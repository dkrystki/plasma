import os
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Optional

from jinja2 import Template
from loguru import logger
from pl.devops import run
from pl.env import Env

import environ

environ = environ.Env()


class App:
    @dataclass
    class Sets:
        name: str
        app_root: Path

    @dataclass
    class Links:
        namespace: "Namespace"

    def __init__(self, se: Sets, li: Links) -> None:
        self.se = se
        self.li = li

        self.env: Optional[Env] = None

    def chdir_to_root(self):
        os.chdir(str(self.se.app_root))

    def deploy(self) -> None:
        logger.info(f"🚀Deploying {self.se.name}.")
        self.chdir_to_root()

    def delete(self) -> None:
        logger.info(f"Delete {self.se.name}.")
        self.chdir_to_root()


class Image:
    @dataclass
    class Sets:
        tag: str

    @dataclass
    class Links:
        env: Env

    def __init__(self, li: Links, se: Sets):
        self.li = li
        self.se = se

    def push(self):
        env = self.li.env
        run(f"""
            docker login {env.registry.address} --username {env.registry.username} -p{env.registry.password}
            docker push {env.registry.address}/{self.se.tag}
            """)


class Dockerfile:
    @dataclass
    class Sets:
        template: Path
        out_path: Path
        base_image: str

    @dataclass
    class Links:
        env: Env

    def __init__(self, li: Links, se: Sets):
        self.li = li
        self.se = se

    def render(self):
        template = Template(self.se.template.read_text())
        env = self.li.env
        context = {
            "env": env,
            "base_image": self.se.base_image
        }
        self.se.out_path.write_text(template.render(**context))

    def build(self, tag: str):
        env = self.li.env
        run(f"""
            docker build -f {str(self.se.out_path)} -t {env.registry.address}/{tag} {env.monorepo_root}
            """)

        return Image(se=Image.Sets(tag=tag),
                     li=Image.Links(env=env))


class PythonUtils:
    @dataclass
    class Sets:
        pass

    @dataclass
    class Links:
        env: Env

    def __init__(self, se: Sets, li: Links) -> None:
        self.se = se
        self.li = li

    def test(self) -> None:
        os.chdir(str(self.li.env.app_src))
        run("poetry run pytest", print_output=True)

    def flake8(self) -> None:
        os.chdir(str(self.li.env.app_root))
        run("flake8", print_output=True)
        logger.info(f"Flaky!")

    def isort(self) -> None:
        os.chdir(str(self.li.env.app_root))
        run("isort -rc .", print_output=True)

    def black(self) -> None:
        os.chdir(str(self.li.env.app_root))
        run("black .", print_output=True)

    def mypy(self) -> None:
        os.chdir(str(self.li.env.app_root))
        logger.info(f"Not implemented!")

    def format(self) -> None:
        self.isort()
        self.black()

    def test_devops(self) -> None:
        os.chdir(str(self.li.env.app_root / "tests/test_devops"))
        run("poetry run pytest", print_output=True)

    def test_bootstrap(self) -> None:
        os.chdir(str(self.li.env.app_root / "tests/test_bootstrap"))
        run("poetry run pytest -s", print_output=True)

    def bootstrap_local_dev(self) -> None:
        os.chdir(str(self.li.env.app_src))
        logger.info(f"Bootstrapping local python development.")
        run(f"""
            poetry config virtualenvs.in-project true
            poetry config virtualenvs.create true
            poetry install
            """, print_output=True)

    def prebuild_image(self) -> None:
        os.chdir(str(self.li.env.app_root))
        logger.info(f"Prebuilding docker image")
        env = self.li.env

        dockerfile = Dockerfile(
            se=Dockerfile.Sets(template=(env.project_comm / "docker/Dockerfile.python.templ"),
                               out_path=Path(f"Dockerfile.{env.stage}.prebuild"),
                               base_image=f"python:{env.python_ver_major}."
                                          f"{env.python_ver_minor}-slim-{env.debian_ver}"),
            li=Dockerfile.Links(env=env)
        )

        dockerfile.render()
        image = dockerfile.build(tag=f"{env.prebuild_image_name}")
        image.push()

        run(f"""
            docker build -f {str(dockerfile.se.out_path)} -t {env.app_name}-prebuild {env.monorepo_root}
            docker tag {env.app_name}-prebuild {env.registry.address}/{env.stage}/flesh/{env.app_name}-prebuild
            docker login {env.registry.address} --username {env.registry.username} -p{env.registry.password}
            docker push {env.registry.address}/{env.stage}/flesh/{env.app_name}-prebuild
            """, print_output=True)


class Skaffold(App):
    @dataclass
    class Sets(App.Sets):
        pass

    @dataclass
    class Links(App.Links):
        pass

    def __init__(self, se: App.Sets, li: App.Links) -> None:
        super().__init__(se, li)
        self.se = se
        self.li = li

        self.dockerfile: Optional[Dockerfile] = None

    def __del__(self):
        Path("skaffold.yaml").unlink(missing_ok=True)

    def deploy(self) -> None:
        super().deploy()

        image_name: str = f"{self.env.registry.address}/{self.env.stage}/{self.li.namespace.name}/{self.se.name}"
        image_tag: str = datetime.now().strftime("%Y-%m-%d_%H_%M_%S")
        os.environ["CG_IMAGE_NAME"] = image_name
        os.environ["CG_IMAGE_TAG"] = image_tag

        self.dockerfile.render()

        # render skaffold.yaml
        image: str = f"{image_name}:{image_tag}"
        template = Template((self.env.project_comm / "kubernetes/skaffold.yaml.templ").read_text())
        skaffold_file = Path(f"skaffold.{self.env.stage}.yaml")
        context = {
            "env": self.env,
            "image_name": image_name,
            "image_tag": image_tag
        }
        skaffold_file.write_text(template.render(**context))

        registry = self.env.registry
        logger.info("Building and deploying using skaffold.")
        run(f"""
            docker login {registry.address} --username {registry.username} -p{registry.password}
            skaffold build -f {str(skaffold_file)} --insecure-registry {self.env.registry.address}
            docker push {image}
            skaffold deploy -f {str(skaffold_file)} --images {image}
            """, print_output=True)

    def skaffold(self) -> None:
        run(f"skaffold dev -p {self.env.stage}", print_output=True)
