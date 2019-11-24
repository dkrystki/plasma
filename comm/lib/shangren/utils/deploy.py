import os
import subprocess

from kubernetes import client, config
from loguru import logger


def run(command: str, ignore_errors=False) -> str:
    try:
        return subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT).decode("utf-8").strip()
    except subprocess.CalledProcessError as e:
        if not ignore_errors:
            output: str = e.stdout.decode('utf-8').strip()
            error_msg: str = f"Command \"{e.cmd}\" produced errozr ({output})"
            raise RuntimeError(error_msg)


def helm_install(namespace: str, name: str, chart: str, version: str, upgrade=True) -> None:
    """
    :param namespace:
    :param name:
    :param chart: chart repository name
    :param version:
    :param upgrade: Try to upgrade when True. Delete and install when False.
    """
    logger.info(f"🚀Deploying {name}")
    if not upgrade:
        try:
            run(f"""helm delete --purge {namespace}-{name}""")
        except RuntimeError:
            pass

    run(f"kubectl create namespace {namespace}", ignore_errors=True)
    run(f"kubectl config set-context minikube --namespace={namespace}")

    run(f"""helm {"upgrade --install" if upgrade else "install"} \
            {"" if upgrade else "--name"} {namespace}-{name} \
            --set fullnameOverride={name} \
            -f values/local/{name}.yaml \
            {"--force" if upgrade else ""} --wait=true \
            --timeout=250s \
            {chart} \
            --version="{version}" \
            """)

    run(f"kubectl config set-context minikube --namespace=default")


def add_pullsecret(namespace: str) -> None:
    logger.info(f"🚀Adding pull secret to {namespace}")
    run(f"""kubectl create secret docker-registry pullsecret -n {namespace} --docker-server=shangren.registry.local \
          --docker-username=user --docker-password=password --docker-email=kwazar90@gmail.com \
          --dry-run -o yaml | kubectl apply -f -""")


def create_namespace(name: str) -> None:
    """
    Create namespace if not exists.
    :param name:
    :return:
    """
    if name not in [ns.metadata.name for ns in kube.list_namespace().items]:
        namespace = client.V1Namespace()
        namespace.metadata = client.V1ObjectMeta(name=name)
        kube.create_namespace(namespace)

config.load_kube_config(
    os.path.join(os.environ["SHANGREN_ROOT"], 'envs/local/kubeconfig.yaml'))

kube = client.CoreV1Api()
