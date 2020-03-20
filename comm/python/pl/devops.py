import collections
import os
import subprocess
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Any, Optional, Type, OrderedDict

import pl.env
from jinja2 import Template
from loguru import logger

import environ

environ = environ.Env()


class CommandError(RuntimeError):
    pass


def run(command: str, ignore_errors: bool = False, print_output: bool = False) -> Optional[str]:
    if environ.bool("PLASMA_DEBUG"):
        logger.debug(command)
    try:
        kwargs: Dict[str, Any] = {}

        if not print_output:
            kwargs["stdout"] = subprocess.PIPE

        p = subprocess.run(command, shell=True, check=True, stderr=subprocess.PIPE, **kwargs)
        if not print_output:
            out = p.stdout.decode('utf-8').strip()
            return out
        else:
            return None
    except subprocess.CalledProcessError as e:
        if not ignore_errors:
            output: str = e.stderr.decode('utf-8').strip()
            error_msg: str = f"Command \"{e.cmd}\" produced error ({output})"
            raise CommandError(error_msg)


class Cluster:
    def __init__(self, env: pl.env.Env) -> None:
        from kubernetes import client, config

        config.load_kube_config(environ.str("KUBECONFIG"))

        self.env: pl.env.Env = env
        self.namespaces: OrderedDict[str, "Namespace"] = collections.OrderedDict()
        self.kube: client.CoreV1Api = client.CoreV1Api()

    def create_namespace(self, name) -> "Namespace":
        namespace = Namespace(
            li=Namespace.Links(cluster=self),
            name=name
        )
        self.namespaces[name] = namespace
        return namespace

    def deploy(self) -> None:
        os.chdir(str(self.env.project_root))
        run("helm repo update")

        n: pl.devops.Namespace
        for n in self.namespaces.values():
            n.deploy()

    def reset(self) -> None:
        os.chdir(str(self.env.project_root))

        n: pl.devops.Namespace
        for n in reversed(self.namespaces.values()):
            if n.exists():
                n.delete()


class Helm:
    """Representation of namespaced helm commands."""

    @dataclass
    class Links:
        namespace: 'Namespace'
        cluster: Cluster

    def __init__(self, li: Links, release_name: str) -> None:
        self.li: Helm.Links = li
        self.release_name = release_name
        self.namespaced_name = f"""{self.li.namespace.name + "-" if self.li.namespace.name else ""}{release_name}"""

    def install(self, chart: str, version: str = None, upgrade: bool = True, repo: str = "") -> None:
        """
        :param repo:
        :param stage:
        :param chart: chart repository name
        :param version: install default if None
        :param upgrade: Try to upgrade when True. Delete and install when False.
        """
        if not upgrade:
            try:
                run(f"""helm delete --purge {self.namespaced_name}""")
            except RuntimeError:
                pass

        if repo:
            run(f"helm repo add {repo}")

        values_path = f"values/{self.li.cluster.env.stage}/{self.release_name}.yaml"

        run(f"""helm {"upgrade --install" if upgrade else "install"} \
                {"" if upgrade else "--name"} {self.namespaced_name} \
                --namespace={self.li.namespace.name} \
                --set fullnameOverride={self.release_name} \
                -f {values_path} \
                {"--force" if upgrade else ""} --wait=true \
                --timeout=250000 \
                "{chart}" \
                {f"--version='{version}'" if version else ""} \
                """)

    def delete(self) -> None:
        logger.info(f"Deleting {self.namespaced_name}")
        run(f"helm delete --purge {self.namespaced_name}")

    def exists(self) -> bool:
        try:
            run(f"helm ls | grep {self.namespaced_name}")
        except CommandError:
            return False
        else:
            return True


class App:
    @dataclass
    class Sets:
        name: str
        app_root: Path

    @dataclass
    class Links:
        cluster: Cluster
        namespace: "Namespace"

    def __init__(self, se: Sets, li: Links) -> None:
        self.se: App.Sets = se
        self.li: App.Links = li

    def deploy(self) -> None:
        logger.info(f"🚀Deploying {self.se.name}.")
        os.chdir(str(self.se.app_root))

    def delete(self) -> None:
        logger.info(f"Delete {self.se.name}.")
        os.chdir(str(self.se.app_root))


class SkaffoldApp(App):
    class Sets(App.Sets):
        pass

    class Links(App.Links):
        pass

    def __init__(self, se: Sets, li: Links) -> None:
        super().__init__(se, li)

    def __del__(self):
        Path("skaffold.yaml").unlink(missing_ok=True)

    def deploy(self) -> None:
        super().deploy()

        env = self.li.cluster.env
        image_name: str = f"{env.registry.address}/{env.stage}/{self.li.namespace.name}/{self.se.name}"
        image_tag: str = datetime.now().strftime("%Y-%m-%d_%H_%M_%S")
        os.environ["CG_IMAGE_NAME"] = image_name
        os.environ["CG_IMAGE_TAG"] = image_tag

        image: str = f"{image_name}:{image_tag}"

        registry = env.registry
        run(f"docker login {registry.address} "
            f"--username {registry.username} -p{registry.password}")

        template = Template(Path("skaffold.yaml.template").read_text())
        skaffold_file = Path("skaffold.yaml")
        context = {
            "env": env,
            "image_name": image_name,
            "image_tag": image_tag
        }
        skaffold_file.write_text(template.render(**context))

        logger.info("Build image using skaffold.")
        run(f"skaffold build", print_output=True)
        run(f"docker push {image}", print_output=True)

        logger.info("Deploy using skaffold.")
        run(f"skaffold deploy "
            f"--images {image}"
            "", print_output=True)

        skaffold_file.unlink()

    def skaffold(self) -> None:
        run(f"skaffold dev -p {self.li.cluster.env.stage}", print_output=True)


class Namespace:
    @dataclass
    class Links:
        cluster: Cluster

    def __init__(self, li: Links, name: str) -> None:
        self.li: Namespace.Links = li
        self.name: str = name
        self.apps: Dict[str, App] = {}

    def create_app(self, name: str, app_cls: Type[App]) -> App:
        app_root = self.li.cluster.env.project_root
        if self.name != "flesh":
            app_root /= self.name
        app_root /= name

        app = app_cls(
            se=app_cls.Sets(name=name, app_root=app_root),
            li=app_cls.Links(cluster=self.li.cluster, namespace=self)
        )
        self.apps[app.se.name] = app
        return app

    def exists(self) -> bool:
        return self.name in [n.metadata.name for n in self.li.cluster.kube.list_namespace().items]

    def deploy(self) -> None:
        self.create()
        for n, a in self.apps.items():
            a.deploy()

    def deploy_app(self, app_name: str) -> None:
        self.create()
        self.apps[app_name].deploy()

    def delete(self) -> None:
        logger.info(f"Deleting namespace {self.name}")
        run(f"kubectl delete namespace {self.name}")

    def kubectl(self, command: str) -> str:
        return run(f"kubectl -n {self.name} {command}")

    def exec(self, pod: str, command: str) -> str:
        return self.kubectl(f'exec {pod} -- bash -c "{command}"')

    def apply_yaml(self, filename: str) -> None:
        self.kubectl(f"apply -f {filename}")

    def delete_yaml(self, filename: str) -> None:
        """
        Delete object specified in a yaml file.

        :param filename: yaml file
        :return:
        """
        self.kubectl(f"delete -f k8s/{filename}")

    def copy(self, src_path: str, dst_path: str) -> None:
        self.kubectl(f"cp {src_path} {dst_path}")

    def get_pods(self) -> List[str]:
        return [p.metadata.name for p in self.li.cluster.kube.list_namespaced_pod(self.name).items]

    def wait_for_pod(self, pod_name: str, timeout: int = 20) -> None:
        """
        :param pod_name:
        :param timeout: Timeout in seconds
        :return:
        """
        self.kubectl(f"wait --for=condition=ready pod {pod_name} --timeout={timeout}s")

    def _add_pullsecret(self) -> None:
        env = self.li.cluster.env
        logger.info(f"🚀Adding pull secret to {self.name}")
        self.kubectl("create secret docker-registry pullsecret "
                     f"--docker-server={env.registry.address} --docker-username={env.registry.username} "
                     f"--docker-password={env.registry.password} --dry-run -o yaml | kubectl apply -f -")

    def create(self, enable_istio: bool = True, add_pull_secret: bool = True) -> None:
        """
        Create namespace if doesn't exist.
        :param enable_istio:
        :param add_pull_secret:
        :return:
        """
        from kubernetes import client

        if self.name not in [ns.metadata.name for ns in self.li.cluster.kube.list_namespace().items]:
            namespace = client.V1Namespace()
            namespace.metadata = client.V1ObjectMeta(name=self.name)
            self.li.cluster.kube.create_namespace(namespace)

        if enable_istio:
            run(f"kubectl label namespace {self.name} istio-injection=enabled --overwrite")

        if add_pull_secret:
            self._add_pullsecret()

    def helm(self, release_name: str) -> Helm:
        """
        Helm factory for a given release.

        :param release_name:
        :return:
        """
        return Helm(li=Helm.Links(namespace=self, cluster=self.li.cluster), release_name=release_name)
