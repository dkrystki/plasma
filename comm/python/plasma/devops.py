import os
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import List, Dict, Any, Optional

import plasma.shell
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
    def __init__(self, env: plasma.shell.Env) -> None:
        from kubernetes import client, config

        config.load_kube_config(environ.str("KUBECONFIG"))

        self.env: plasma.shell.Env = env
        self.namespaces: Dict[str, "Namespace"] = {}
        self.apps: List[App] = []
        self.kube: client.CoreV1Api = client.CoreV1Api()

    def add_namespace(self, namespace: 'Namespace') -> None:
        self.namespaces[namespace.name] = namespace

    def deploy(self):
        for a in self.apps:
            a.deploy()

    def delete(self):
        for a in self.apps:
            a.delete()


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

    def install(self, chart: str, version: str = None, upgrade=True) -> None:
        """
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


class Namespace:
    @dataclass
    class Links:
        cluster: Cluster

    def __init__(self, li: Links, name: str) -> None:
        self.li: Namespace.Links = li
        self.name: str = name

    def kubectl(self, command: str) -> str:
        return run(f"kubectl -n {self.name} {command}")

    def exec(self, pod: str, command: str) -> str:
        return self.kubectl(f'exec {pod} -- bash -c "{command}"')

    def apply(self, filename: str) -> None:
        self.kubectl(f"apply -f k8s/{filename}")

    def delete(self, filename: str) -> None:
        """
        Delete object specified in a yaml file.

        :param filename: yaml file
        :return:
        """
        self.kubectl(f"delete -f k8s/{filename}")

    def copy(self, src_path: str, dst_path: str):
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
        logger.info(f"🚀Adding pull secret to {self.name}")
        run(f"""kubectl create secret docker-registry pullsecret -n \
                {self.name} --docker-server=shangren.registry.local \
              --docker-username=user --docker-password=password --docker-email=kwazar90@gmail.com \
              --dry-run -o yaml | kubectl apply -f -""")

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


class App:
    @dataclass
    class Links:
        cluster: Cluster
        namespace: Namespace

    def __init__(self, name: str, li: Links) -> None:
        self.name: str = name
        self.li: App.Links = li
        self.app_root: Path = Path()

    def deploy(self) -> None:
        logger.info(f"🚀Deploying {self.name}.")
        os.chdir(str(self.app_root))

    def delete(self) -> None:
        logger.info(f"Delete {self.name}.")
        os.chdir(str(self.app_root))
