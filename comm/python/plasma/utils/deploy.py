import os
import subprocess
from typing import List

from kubernetes import client, config
from loguru import logger

import environ

env = environ.Env()

config.load_kube_config(
    os.path.join(os.environ["PROJECT_ROOT"], 'envs/local/kubeconfig.yaml'))

kube = client.CoreV1Api()

PLASMA_DEBUG: bool = env.bool("PLASMA_DEBUG")


class CommandError(RuntimeError):
    pass


def run(command: str, ignore_errors=False) -> str:
    try:
        if PLASMA_DEBUG:
            logger.debug(command)
        return subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT).decode("utf-8").strip()
    except subprocess.CalledProcessError as e:
        if not ignore_errors:
            output: str = e.stdout.decode('utf-8').strip()
            error_msg: str = f"Command \"{e.cmd}\" produced error ({output})"
            raise CommandError(error_msg)


class Helm:
    """Namespaced helm representation."""

    def __init__(self, namespace: 'Namespace', release_name: str) -> None:
        self.namespace = namespace
        self.release_name = release_name
        self.namespaced_name = f"""{self.namespace.name + "-" if self.namespace.name else ""}{release_name}"""

    def install(self, chart: str, values_path: str = "Default", version: str = None, upgrade=True) -> None:
        """
        :param values_path:
        :param chart: chart repository name
        :param version: install default if None
        :param upgrade: Try to upgrade when True. Delete and install when False.
        """
        logger.info(f"🚀Deploying {self.release_name}")
        if not upgrade:
            try:
                run(f"""helm delete --purge {self.namespaced_name}""")
            except RuntimeError:
                pass

        if values_path == "Default":
            values_path = f"values/local/{self.release_name}.yaml"

        run(f"""helm {"upgrade --install" if upgrade else "install"} \
                {"" if upgrade else "--name"} {self.namespaced_name} \
                --namespace={self.namespace.name} \
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
    def __init__(self, name: str) -> None:
        self.name: str = name

    def kubectl(self, command: str) -> str:
        return run(f"kubectl -n {self.name} {command}")

    def exec(self, pod: str, command: str) -> str:
        return self.kubectl(f'exec {pod} -- bash -c "{command}"')

    def apply(self, filename: str) -> None:
        self.kubectl(f"apply -f k8s/{filename}")

    def copy(self, src_path: str, dst_path: str):
        self.kubectl(f"cp {src_path} {dst_path}")

    def get_pods(self) -> List[str]:
        return [p.metadata.name for p in kube.list_namespaced_pod(self.name).items]

    def wait_for_pod(self, pod_name: str, timeout: int = 20) -> None:
        """
        :param pod_name:
        :param timeout: Timeout in seconds
        :return:
        """
        self.kubectl(f"wait --for=condition=ready pod {pod_name} --timeout={timeout}s")

    def _add_pullsecret(self) -> None:
        logger.info(f"🚀Adding pull secret to {self.name}")
        run(f"""kubectl create secret docker-registry pullsecret -n {self.name} --docker-server=shangren.registry.local \
              --docker-username=user --docker-password=password --docker-email=kwazar90@gmail.com \
              --dry-run -o yaml | kubectl apply -f -""")

    def create(self, enable_istio: bool = True, add_pull_secret: bool = True) -> None:
        """
        Create namespace if doesn't exist.
        :param enable_istio:
        :param add_pull_secret:
        :return:
        """
        if self.name not in [ns.metadata.name for ns in kube.list_namespace().items]:
            namespace = client.V1Namespace()
            namespace.metadata = client.V1ObjectMeta(name=self.name)
            kube.create_namespace(namespace)

        if enable_istio:
            run(f"kubectl label namespace {self.name} istio-injection=enabled --overwrite")

        if add_pull_secret:
            logger.info(f"🚀Adding pull secret to {self.name}")
            run(f"""kubectl create secret docker-registry pullsecret -n {self.name} \
            --docker-server=shangren.registry.local \
            --docker-username=user --docker-password=password --docker-email=kwazar90@gmail.com \
                          --dry-run -o yaml | kubectl apply -f -""")

    def helm(self, release_name: str) -> Helm:
        """
        Helm factory for a given release.

        :param release_name:
        :return:
        """
        return Helm(namespace=self, release_name=release_name)
