import os
import subprocess

from kubernetes import client, config
from loguru import logger


config.load_kube_config(
    os.path.join(os.environ["SHANGREN_ROOT"], 'envs/local/kubeconfig.yaml'))

kube = client.CoreV1Api()


def run(command: str, ignore_errors=False) -> str:
    try:
        return subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT).decode("utf-8").strip()
    except subprocess.CalledProcessError as e:
        if not ignore_errors:
            output: str = e.stdout.decode('utf-8').strip()
            error_msg: str = f"Command \"{e.cmd}\" produced errozr ({output})"
            raise RuntimeError(error_msg)


class Namespace:
    def __init__(self, name: str, enable_istio: bool = True, add_pull_secret: bool = True):
        self.name: str = name
        self._create()

        if enable_istio:
            self._enable_istio()

        if add_pull_secret:
            self._add_pullsecret()

    def kubectl(self, command: str) -> str:
        return run(f"kubectl -n {self.name} {command}")

    def helm_install(self, release_name: str, chart: str, version: str, upgrade=True) -> None:
        """
        :param namespace:
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

        run(f"kubectl create namespace {self.name}", ignore_errors=True)
        run(f"kubectl config set-context minikube --namespace={self.name}")

        namespaced_name = f"""{self.name + "-" if self.name else ""}{release_name}"""
        run(f"""helm {"upgrade --install" if upgrade else "install"} \
                {"" if upgrade else "--name"} {namespaced_name} \
                --set fullnameOverride={release_name} \
                -f values/local/{release_name}.yaml \
                {"--force" if upgrade else ""} --wait=true \
                --timeout=250000 \
                "{chart}" \
                --version="{version}" \
                """)

        run(f"kubectl config set-context minikube --namespace=default")

    def _enable_istio(self) -> None:
        run(f"kubectl label namespace {self.name} istio-injection=enabled --overwrite")

    def _add_pullsecret(self) -> None:
        logger.info(f"🚀Adding pull secret to {self.name}")
        run(f"""kubectl create secret docker-registry pullsecret -n {self.name} --docker-server=shangren.registry.local \
              --docker-username=user --docker-password=password --docker-email=kwazar90@gmail.com \
              --dry-run -o yaml | kubectl apply -f -""")

    def _create(self) -> None:
        """
        Create namespace if doesn't exist.
        :param name:
        :return:
        """
        if self.name not in [ns.metadata.name for ns in kube.list_namespace().items]:
            namespace = client.V1Namespace()
            namespace.metadata = client.V1ObjectMeta(name=self.name)
            kube.create_namespace(namespace)
