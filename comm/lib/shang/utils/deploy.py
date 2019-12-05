import os
import subprocess

from kubernetes import client, config
from loguru import logger

import environ
env = environ.Env()


config.load_kube_config(
    os.path.join(os.environ["SHANGREN_ROOT"], 'envs/local/kubeconfig.yaml'))

kube = client.CoreV1Api()

DEBUG: bool = env.bool("SHANG_DEBUG")


def run(command: str, ignore_errors=False) -> str:
    try:
        if DEBUG:
            logger.debug(command)
        return subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT).decode("utf-8").strip()
    except subprocess.CalledProcessError as e:
        if not ignore_errors:
            output: str = e.stdout.decode('utf-8').strip()
            error_msg: str = f"Command \"{e.cmd}\" produced errozr ({output})"
            raise RuntimeError(error_msg)


class Namespace:
    def __init__(self, name: str):
        self.name: str = name

    def kubectl(self, command: str) -> str:
        return run(f"kubectl -n {self.name} {command}")

    def exec(self, pod: str, command: str) -> str:
        return self.kubectl(f'exec {pod} -- bash -c "{command}"')

    def apply(self, filename: str) -> None:
        self.kubectl(f"apply -f k8s/{filename}")

    def copy(self, src_path: str, dst_path: str):
        self.kubectl(f"cp {src_path} {dst_path}")

    def wait_for_pod(self, pod_name: str, timeout: int = 20) -> None:
        """
        :param pod_name:
        :param timeout: Timeout in seconds
        :return:
        """
        self.kubectl(f"wait --for=condition=ready pod {pod_name} --timeout={timeout}s")

    def helm_install(self, release_name: str, chart: str, version: str, upgrade=True) -> None:
        """
        :param release_name:
        :param chart: chart repository name
        :param version:
        :param upgrade: Try to upgrade when True. Delete and install when False.
        """
        logger.info(f"🚀Deploying {release_name}")
        if not upgrade:
            try:
                run(f"""helm delete --purge {self.name}-{release_name}""")
            except RuntimeError:
                pass

        namespaced_name = f"""{self.name + "-" if self.name else ""}{release_name}"""
        run(f"""helm {"upgrade --install" if upgrade else "install"} \
                {"" if upgrade else "--name"} {namespaced_name} \
                --namespace={self.name} \
                --set fullnameOverride={release_name} \
                -f values/local/{release_name}.yaml \
                {"--force" if upgrade else ""} --wait=true \
                --timeout=250000 \
                "{chart}" \
                --version="{version}" \
                """)

    def helm_delete(self, release_name: str) -> None:
        logger.info(f"Deleting {release_name}")
        namespaced_name = f"""{self.name + "-" if self.name else ""}{release_name}"""
        run(f"helm delete --purge {namespaced_name}")

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
            run(f"""kubectl create secret docker-registry pullsecret -n {self.name} --docker-server=shangren.registry.local \
                          --docker-username=user --docker-password=password --docker-email=kwazar90@gmail.com \
                          --dry-run -o yaml | kubectl apply -f -""")

