import os
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

from jinja2 import Template
from loguru import logger

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..cluster import ClusterEnv

from ..devops import run
from ..env import Env

import environ

environ = environ.Env()


class AppEnv(Env):
    app_name: str = None
    src: Path = None
    cluster: "ClusterEnv" = None
    prebuild: bool = None
    helm_release_name: str = None
    src_image: str = None
    dockerfile_templ: Path = None
    image_name: str = None

    def __init__(self):
        super().__init__()
        self.src = self.root / "flesh"

        self.prebuild_image_name = f"{self.cluster.registry.address}/{self.stage}/{self.app_name}-prebuild:latest"

        if self.prebuild:
            self.base_image = f"{self.prebuild_image_name}"
        else:
            self.base_image = self.src_image

        self.image_name: str = f"{self.cluster.registry.address}/{self.stage}/{self.app_name}"

    def activate(self) -> None:
        self.cluster.activate()
        super().activate()
        self._set_environ("HELM_RELEASE_NAME", str(self.helm_release_name))
        self._set_environ("APP_SRC", str(self.src))


class App:
    @dataclass
    class Sets:
        name: str
        root: Path

    @dataclass
    class Links:
        namespace: "Namespace"

    def __init__(self, se: Sets, li: Links) -> None:
        self.se = se
        self.li = li

        self.env: AppEnv

    def chdir_to_root(self):
        os.chdir(str(self.se.root))

    def deploy(self) -> None:
        # TODO: only create when needed
        self.li.namespace.create()
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
        env: AppEnv

    def __init__(self, li: Links, se: Sets):
        self.li = li
        self.se = se

    def push(self):
        env = self.li.env
        run(f"""
            docker login {env.cluster.registry.address} \\
            --username {env.cluster.registry.username} -p{env.cluster.registry.password}
            docker push {self.se.tag}
            """, print_output=False)


class Dockerfile:
    @dataclass
    class Sets:
        template: Path
        out_path: Path
        base_image: str

    @dataclass
    class Links:
        env: AppEnv

    def __init__(self, li: Links, se: Sets):
        self.li = li
        self.se = se

    def render(self):
        template = Template(self.se.template.read_text())
        env = self.li.env
        context = {
            "env": env,
            "base_image": f"{self.se.base_image}"
        }
        self.se.out_path.write_text(template.render(**context))

    def build(self, tag: str):
        os.chdir(str(self.li.env.root))
        env = self.li.env
        run(f"""
            docker build -f {str(self.se.out_path)} -t {tag} {env.cluster.plasma.root}
            """, print_output=False)

        return Image(se=Image.Sets(tag=tag),
                     li=Image.Links(env=env))


class DockerUtils:
    @dataclass
    class Sets:
        pass

    @dataclass
    class Links:
        env: AppEnv
        dockerfile: Dockerfile

    def __init__(self, se: Sets, li: Links) -> None:
        self.se = se
        self.li = li

    def prebuild(self) -> None:
        logger.info(f"Prebuilding {self.li.env.app_name}...")
        os.chdir(str(self.li.env.root))
        env = self.li.env
        dockerfile = Dockerfile(
            se=Dockerfile.Sets(template=self.li.dockerfile.se.template,
                               out_path=Path(f"{self.li.dockerfile.se.out_path}.prebuild"),
                               base_image=env.src_image),
            li=Dockerfile.Links(env=env)
        )
        dockerfile.render()
        image = dockerfile.build(tag=env.prebuild_image_name)
        image.push()


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

    def flake8(self) -> None:
        os.chdir(str(self.li.env.root))
        run("flake8", print_output=True)
        logger.info(f"Flaky!")

    def isort(self) -> None:
        os.chdir(str(self.li.env.root))
        run("isort -rc .", print_output=True)

    def black(self) -> None:
        os.chdir(str(self.li.env.root))
        run("black .", print_output=True)

    def mypy(self) -> None:
        os.chdir(str(self.li.env.root))
        logger.info(f"Not implemented!")

    def format(self) -> None:
        self.isort()
        self.black()

    def test_devops(self) -> None:
        os.chdir(str(self.li.env.root / "tests/test_devops"))
        run("poetry run pytest", print_output=True)


class AppPythonUtils(PythonUtils):
    @dataclass
    class Sets(PythonUtils.Sets):
        pass

    @dataclass
    class Links(PythonUtils.Links):
        env: AppEnv

    def __init__(self, se: Sets, li: Links) -> None:
        super().__init__(se, li)
        self.se = se
        self.li = li

    def test(self) -> None:
        os.chdir(str(self.li.env.src))
        run("poetry run pytest", print_output=True)

    def bootstrap_local_dev(self) -> None:
        os.chdir(str(self.li.env.src))
        logger.info(f"Bootstrapping local python development.")
        run(f"""
            poetry config virtualenvs.in-project true
            poetry config virtualenvs.create true
            poetry install
            """, print_output=True)


class NodeUtils:
    @dataclass
    class Sets:
        pass

    @dataclass
    class Links:
        env: AppEnv

    def __init__(self, se: Sets, li: Links) -> None:
        self.se = se
        self.li = li

    def test(self) -> None:
        os.chdir(str(self.li.env.src))
        raise NotImplementedError()

    def test_devops(self) -> None:
        raise NotImplementedError()

    def test_bootstrap(self) -> None:
        raise NotImplementedError()

    def bootstrap_local_dev(self) -> None:
        raise NotImplementedError()


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

        self.env: AppEnv

        self.dockerfile = Dockerfile(
            se=Dockerfile.Sets(template=self.env.dockerfile_templ,
                               out_path=Path(f"Dockerfile.{self.env.stage}"),
                               base_image=self.env.base_image),
            li=Dockerfile.Links(env=self.env)
        )
        self.skaffold_file = Path(f"skaffold.{self.env.stage}.yaml")

    def render(self) -> None:
        self.chdir_to_root()

        self.dockerfile.render()

        template = Template((self.env.cluster.comm / "kubernetes/skaffold.yaml.templ").read_text())
        context = {
            "env": self.env,
            "image_name": self.env.image_name,
        }
        self.skaffold_file.write_text(template.render(**context))

    def deploy(self) -> None:
        super().deploy()
        self.render()

        registry = self.env.cluster.registry
        logger.info("Building and deploying using skaffold.")

        os.environ["PL_IMAGE_NAME"] = self.env.image_name
        image_tag: str = datetime.now().strftime("%Y-%m-%d_%H_%M_%S")
        os.environ["PL_IMAGE_TAG"] = image_tag

        image = f"{self.env.image_name}:{image_tag}"

        run(f"""
            docker login {registry.address} --username {registry.username} -p{registry.password}
            skaffold build -f {str(self.skaffold_file)} --insecure-registry {registry.address}
            docker push {image}
            skaffold deploy -f {str(self.skaffold_file)} --images {image}
            """, print_output=True)

    def skaffold(self) -> None:
        self.render()
        registry = self.env.cluster.registry
        run(f"""
            docker login {registry.address} --username {registry.username} -p{registry.password}
            skaffold dev -f {str(self.skaffold_file)}
            """, print_output=True)
