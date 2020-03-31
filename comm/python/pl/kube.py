from dataclasses import dataclass
from typing import List, Dict, Any, Type

from kubernetes import client
from loguru import logger

import environ
from pl.apps import App
from pl.devops import run, CommandError

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from env import Env

environ = environ.Env()


class HelmRelease:
    """Representation of namespaced helm commands."""

    @dataclass
    class Links:
        namespace: 'Namespace'
        env: "Env"

    def __init__(self, li: Links, release_name: str) -> None:
        self.li: HelmRelease.Links = li
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

        values_path = f"values/{self.li.env.stage}/{self.release_name}.yaml"

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


class Pod:
    @dataclass
    class Sets:
        name: str

    @dataclass
    class Links:
        app: "App"

    def __init__(self, se: Sets, li: Links):
        self.se = se
        self.li = li

    def exec(self, command: str, print_output: bool = False) -> str:
        return self.li.app.li.namespace.exec(pod=self.se.name, command=command, print_output=print_output)

    def copy_from_pod(self, src_path: str, dst_path: str) -> None:
        return self.li.app.li.namespace.copy(src_path=f"{self.se.name}:{src_path}", dst_path=dst_path)

    def copy_to_pod(self, src_path: str, dst_path: str) -> None:
        return self.li.app.li.namespace.copy(src_path=src_path, dst_path=f"{self.se.name}:{dst_path}")


class Namespace:
    @dataclass
    class Links:
        kube: client.CoreV1Api
        env: "Env"

    def __init__(self, li: Links, name: str) -> None:
        self.li = li
        self.name = name
        self.apps: Dict[str, App] = {}

    def create_app(self, name: str, app_cls: Type[App], extra_links: Dict[str, Any] = None) -> Any:
        app_root = self.li.env.project_root
        if self.name != "flesh":
            app_root /= self.name
        app_root /= name

        if not extra_links:
            extra_links = {}

        app = app_cls(
            se=app_cls.Sets(name=name, app_root=app_root),
            li=app_cls.Links(namespace=self, **extra_links)
        )
        self.apps[app.se.name] = app
        return app

    def exists(self) -> bool:
        return self.name in [n.metadata.name for n in self.li.kube.list_namespace().items]

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

    def kubectl(self, command: str, print_output: bool = False) -> List[str]:
        return run(f"kubectl -n {self.name} {command}", print_output=print_output)

    def exec(self, pod: str, command: str, print_output: bool = False) -> List[str]:
        return self.kubectl(f'exec {pod} -- bash -c "{command}"', print_output=print_output)

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
        return [p.metadata.name for p in self.li.kube.list_namespaced_pod(self.name).items]

    def wait_for_pod(self, pod_name: str, timeout: int = 20) -> None:
        """
        :param pod_name:
        :param timeout: Timeout in seconds
        :return:
        """
        self.kubectl(f"wait --for=condition=ready pod {pod_name} --timeout={timeout}s")

    def _add_pullsecret(self) -> None:
        env = self.li.env
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

        if self.name not in [ns.metadata.name for ns in self.li.kube.list_namespace().items]:
            namespace = client.V1Namespace()
            namespace.metadata = client.V1ObjectMeta(name=self.name)
            self.li.kube.create_namespace(namespace)

        if enable_istio:
            run(f"kubectl label namespace {self.name} istio-injection=enabled --overwrite")

        if add_pull_secret:
            self._add_pullsecret()

    def helm(self, release_name: str) -> HelmRelease:
        """
        Helm factory for a given release.

        :param release_name:
        :return:
        """
        return HelmRelease(li=HelmRelease.Links(namespace=self, env=self.li.env), release_name=release_name)
