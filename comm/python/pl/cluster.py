import collections
import os
import re
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import OrderedDict, Optional

from . import env
from jinja2 import Template
from loguru import logger

from . import apps

import environ
from .devops import run
from .kube import Namespace

environ = environ.Env()


@dataclass
class ClusterEnv(env.Env):
    @dataclass
    class Device(env.BaseEnv):
        k8s_ver: str = None
        name: str = None
        ip: str = ""

    @dataclass
    class Registry(env.BaseEnv):
        address: str = None
        username: str = None
        password: str = None
        ip: str = ""

    skaffold_ver: str = None
    kubectl_ver: str = None
    helm_ver: str = None
    kind_ver: str = None
    debian_ver: str = None
    docker_ver: str = None
    device: Device = None
    registry: Registry = None
    plasma: env.Env = None
    deps_path: Path = None

    def __init__(self):
        super().__init__()

        self.deps_path = self.root / Path(".deps")
        self.kubeconfig = self.root / f"envs/{self.stage}/kubeconfig.yaml"
        self.comm: Path = self.root / "comm"

    def activate(self) -> None:
        super().activate()

        self.deps_path.mkdir(exist_ok=True)
        self._set_environ("DEPS_PATH", str(self.deps_path))

        self._set_environ("STAGE", self.stage)
        self._set_environ("EMOJI", self.emoji)

        self._set_environ("PROJECT_ROOT", str(self.root))
        self._set_environ("PROJECT_NAME", str(self.name))

        self._set_environ("DEBIAN_VER", self.debian_ver)
        self._set_environ("SKAFFOLD_VER", self.skaffold_ver)
        self._set_environ("KUBECTL_VER", self.kubectl_ver)
        self._set_environ("HELM_VER", self.helm_ver)
        self._set_environ("KIND_VER", self.kind_ver)
        self._set_environ("DOCKER_VER", self.docker_ver)

        self._set_environ("DEVICE_NAME", self.device.name)
        self._set_environ("DEVICE_IP", self.device.ip)
        self._set_environ("DEVICE_K8S_VER", str(self.device.k8s_ver))

        self._set_environ("REGISTRY_ADDRESS", self.registry.address)
        self._set_environ("REGISTRY_USERNAME", self.registry.username)
        self._set_environ("REGISTRY_PASSWORD", self.registry.password)
        self._set_environ("REGISTRY_IP", self.registry.ip)

        os.environ["PATH"] = f"{str(self.deps_path)}:{os.environ['PATH']}"
        os.environ["PYTHONPATH"] = f"{str(self.comm)}/python:{os.environ['PATH']}"
        os.environ["KUBECONFIG"] = str(self.kubeconfig)

        self.plasma.activate()

    def chdir_to_cluster_root(self) -> None:
        os.chdir(str(self.root))


class ClusterDevice:
    def __init__(self, env: ClusterEnv):
        self.env = env

    def bootstrap(self) -> None:
        pass

    def _post_bootstrap(self) -> None:
        logger.info("Initializing helm")
        run(f""" 
        helm init --wait --tiller-connection-timeout 600
        kubectl apply -f {self.env.plasma.comm}/k8s/ingress-rbac.yaml
        kubectl apply -f {self.env.plasma.comm}/k8s/rbac-storage-provisioner.yaml
        kubectl create serviceaccount -n kube-system tiller
        kubectl create clusterrolebinding tiller-cluster-admin \\
            --clusterrole=cluster-admin --serviceaccount=kube-system:tiller
        kubectl --namespace kube-system patch deploy tiller-deploy -p \\
            '{{"spec":{{"template":{{"spec":{{"serviceAccount":"tiller"}} }} }} }}'
        """, progress_bar=True)

    def get_ip(self) -> str:
        raise NotImplementedError()


class Kind(ClusterDevice):
    def __init__(self, env: ClusterEnv):
        super().__init__(env)

    def bootstrap(self) -> None:
        super().bootstrap()

        logger.info("Creating kind cluster")

        template = Template(Path("kind.yaml.template").read_text())
        kind_file = Path(f"kind.{self.env.stage}.yaml")
        context = {"env": self.env}
        kind_file.write_text(template.render(**context))

        Path(environ.str("KUBECONFIG")).unlink(missing_ok=True)
        run(f"""
            kind delete cluster --name={self.env.device.name}
            kind create cluster --config={str(kind_file)} --name={self.env.device.name}
            """, progress_bar=True)

        ip = self.get_ip()

        run(f"""
            docker exec {self.env.device.name}-control-plane bash -c "echo \\"{ip} \\
            {self.env.registry.address}\\" >> /etc/hosts" 
            # For some reason dns resolution doesn't work on CI. This line fixes it
            docker exec {self.env.device.name}-control-plane \\
            bash -c "echo \\"nameserver 8.8.8.8\\" >> /etc/resolv.conf" 
            """, progress_bar=True)

        self._post_bootstrap()

    def get_ip(self) -> str:
        result = run(f"""kubectl describe nodes {self.env.device.name}""")
        ip_phrase = re.search(r"InternalIP: .*", "\n".join(result)).group(0)
        ip = ip_phrase.split(":")[1].strip()
        return ip.strip()


class Microk8s(ClusterDevice):
    def __init__(self, env: env.Env):
        super().__init__(env)

    def bootstrap(self) -> None:
        super().bootstrap()

        logger.info("Creating microk8s cluster")

        Path(environ.str("KUBECONFIG")).unlink(missing_ok=True)
        run(f"""
        sudo snap remove microk8s
        sudo snap install microk8s --classic --channel="{self.env.device.k8s_ver}"/stable
        sudo sed -i "s/local.insecure-registry.io/{self.env.registry.address}/g" \\ 
            /var/snap/microk8s/current/args/containerd-template.toml
        sudo sed -i "s/http:\/\/localhost:32000/http:\/\/{self.env.registry.address}/g" \\
            /var/snap/microk8s/current/args/containerd-template.toml
        sudo microk8s.start

        mkdir -p "$(dirname "$KUBECONFIG")"
        sudo microk8s.config > "$KUBECONFIG"

        sudo microk8s.enable dns
        sudo microk8s.enable rbac
        sudo microk8s.enable storage
        sudo microk8s.enable ingress

        sudo sh -c 'echo "--allow-privileged=true" >> /var/snap/microk8s/current/args/kube-apiserver'
        sudo systemctl restart snap.microk8s.daemon-apiserver.service
        """, progress_bar=True)

        time.sleep(30)

        self._post_bootstrap()

    def get_ip(self) -> str:
        return "127.0.0.1"


class AwsCluster(ClusterDevice):
    def bootstrap(self) -> None:
        """eksctl create cluster --name prod --region ap-southeast-1 --nodegroup-name standard-workers
        --node-type t3.medium --nodes 1 --nodes-min 1 --nodes-max 1 --ssh-access --ssh-public-key
         ~/.ssh/id_rsa.pub --managed"""

    def get_ip(self) -> str:
        return ""


class Cluster:
    @dataclass
    class Links:
        device: ClusterDevice

    @dataclass
    class Sets:
        deploy_ingress: bool = True

    def __init__(self, li: Links, se: Sets, env: ClusterEnv) -> None:
        from pl.apps.ingress import Ingress
        from pl.apps.registry import Registry

        from kubernetes import client, config
        self.li = li
        self.se = se
        self.env = env

        self.namespaces: OrderedDict[str, Namespace] = collections.OrderedDict()

        if "KUBECONFIG" in environ and Path(environ.str("KUBECONFIG")).exists():
            config.load_kube_config(environ.str("KUBECONFIG"))
        self.kube: client.CoreV1Api = client.CoreV1Api()

        self.python = apps.PythonUtils(se=apps.PythonUtils.Sets(),
                                       li=apps.PythonUtils.Links(env=self.env))

        self.system = self.create_namespace("system")
        if self.se.deploy_ingress:
            self.system.create_app("ingress", Ingress)

        self.system.create_app("registry", Registry)

    def is_ci_job(self) -> bool:
        return "CI_JOB_ID" in environ

    def sudo(self) -> str:
        if self.is_ci_job():
            return ""
        else:
            return "sudo"

    def chdir_to_project_root(self) -> None:
        os.chdir(str(self.env.root))

    def create_namespace(self, name) -> Namespace:
        namespace = Namespace(

            li=Namespace.Links(
                env=self.env,
                kube=self.kube
            ),
            name=name
        )
        self.namespaces[name] = namespace
        return namespace

    def prebuild_all(self) -> None:
        logger.info("Prebuilding images.")

    def deploy(self) -> None:
        self.chdir_to_project_root()
        run("helm repo update")

        self.system.deploy()

        self.prebuild_all()

        n: Namespace
        for n in self.namespaces.values():
            if n.name == "system":
                continue

            n.deploy()

    def add_hosts(self):
        logger.info("Adding hosts to /etc/hosts file")

    def reset(self) -> None:
        self.chdir_to_project_root()

        n: Namespace
        for n in reversed(self.namespaces.values()):
            if n.exists():
                n.delete()

    def install_deps(self) -> None:
        self.chdir_to_project_root()

    def install_helm(self) -> None:
        self.chdir_to_project_root()
        logger.info("Installing helm")

        if (Path(self.env.deps_path)/"helm").exists():
            logger.info("Already exists, passing.")
            return

        release_name = f"helm-v{self.env.helm_ver}-linux-386"
        run(f"""
            cd /tmp
            curl -Lso helm.tar.gz https://get.helm.sh/{release_name}.tar.gz
            tar -zxf helm.tar.gz
            mv linux-386/helm {self.env.deps_path}/helm
            """, progress_bar=True)
        logger.info("Done")

    def install_kind(self) -> None:
        self.chdir_to_project_root()
        logger.info("Installing kind")

        if (Path(self.env.deps_path)/"kind").exists():
            logger.info("Already exists, passing.")
            return

        run(f"""
            cd /tmp
            curl -Lso kind \\
                "https://github.com/kubernetes-sigs/kind/releases/download/v{self.env.kind_ver}/kind-$(uname)-amd64"
            chmod +x kind
            mv kind {self.env.deps_path}/kind
            """, progress_bar=True)

    def install_kubectl(self) -> None:
        self.chdir_to_project_root()
        logger.info("Installing kubectl")

        if (Path(self.env.deps_path)/"kubectl").exists():
            logger.info("Already exists, passing.")
            return

        run(f"""
            cd /tmp
            curl -Lso kubectl \\
            "https://storage.googleapis.com/kubernetes-release/release/v{self.env.kubectl_ver}/bin/linux/amd64/kubectl"
            chmod +x kubectl
            mv kubectl {self.env.deps_path}/kubectl
            """, progress_bar=True)
        logger.info("Done")

    def install_skaffold(self) -> None:
        self.chdir_to_project_root()
        logger.info("Installing skaffold")

        if (Path(self.env.deps_path)/"skaffold").exists():
            logger.info("Already exists, passing.")
            return

        run(f"""
            cd /tmp
            curl -Lso skaffold \\
                "https://storage.googleapis.com/skaffold/releases/v{self.env.skaffold_ver}/skaffold-linux-amd64"
            chmod +x skaffold
            mv skaffold {self.env.deps_path}/skaffold
            """, progress_bar=True)
        logger.info("Done")

    def install_hostess(self) -> None:
        self.chdir_to_project_root()
        logger.info("Installing hostess")

        if (Path(self.env.deps_path)/"hostess").exists():
            logger.info("Already exists, passing.")
            return

        run(f"""
            cd /tmp
            curl -Lso hostess https://github.com/cbednarski/hostess/releases/download/v0.3.0/hostess_linux_386
            chmod u+x hostess
            mv hostess {self.env.deps_path}/hostess
            """, progress_bar=True)
        logger.info("Done")

    def bootstrap(self) -> None:
        # TODO: Disable this on prod
        self.chdir_to_project_root()
        logger.info(f"Bootstraping {self.env.stage} cluster")

        self.li.device.bootstrap()
        self.add_hosts()

        logger.info("Cluster is ready")

    def test_bootstrap(self) -> None:
        os.chdir(str(self.env.root / "tests/test_bootstrap"))
        run("poetry run pytest -s", print_output=True)
