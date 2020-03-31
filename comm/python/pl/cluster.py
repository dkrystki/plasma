import collections
import os
import time
from dataclasses import dataclass
from pathlib import Path
from typing import OrderedDict

import pl.env
from jinja2 import Template
from loguru import logger

from pl import apps

import environ
from pl.devops import run
from pl.kube import Namespace

environ = environ.Env()


class ClusterDevice:
    def __init__(self, env: pl.env.Env):
        self.env = env

    def bootstrap(self) -> None:
        pass

    def _post_bootstrap(self) -> None:
        logger.info("Initializing helm")
        run(f""" 
        helm init --wait --tiller-connection-timeout 600
        kubectl apply -f {self.env.comm_root}/k8s/ingress-rbac.yaml
        kubectl apply -f {self.env.comm_root}/k8s/rbac-storage-provisioner.yaml
        kubectl create serviceaccount -n kube-system tiller
        kubectl create clusterrolebinding tiller-cluster-admin \\
            --clusterrole=cluster-admin --serviceaccount=kube-system:tiller
        kubectl --namespace kube-system patch deploy tiller-deploy -p \\
            '{{"spec":{{"template":{{"spec":{{"serviceAccount":"tiller"}} }} }} }}'
        """, progress_bar=True)

    def get_ip(self) -> str:
        raise NotImplementedError()


class Kind(ClusterDevice):
    def __init__(self, env: pl.env.Env):
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
        kind delete cluster --name={self.env.cluster.name}
        kind create cluster --config={str(kind_file)} --name={self.env.cluster.name}
        docker exec {self.env.cluster.name}-control-plane bash -c "echo \\"{self.env.registry.ip} \\
        {self.env.registry.address}\\" >> /etc/hosts" 
        # For some reason dns resolution doesn't work on CI. This line fixes it
        docker exec {self.env.cluster.name}-control-plane \\
        bash -c "echo \\"nameserver 8.8.8.8\\" >> /etc/resolv.conf" 
        """, progress_bar=True)

        self._post_bootstrap()

    def get_ip(self) -> str:
        ip = run(f"""
            kubectl describe nodes {self.env.cluster.name} | \\
            grep -oP "InternalIP:  \K.*" 
            """)[0]
        return ip.strip()


class Microk8s(ClusterDevice):
    def __init__(self, env: pl.env.Env):
        super().__init__(env)

    def bootstrap(self) -> None:
        super().bootstrap()

        logger.info("Creating microk8s cluster")

        Path(environ.str("KUBECONFIG")).unlink(missing_ok=True)
        run(f"""
        sudo snap remove microk8s
        sudo snap install microk8s --classic --channel="{self.env.cluster.kubernetes_ver}"/stable
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

    def __init__(self, li: Links, env: pl.env.Env) -> None:
        from kubernetes import client, config
        self.li = li
        self.env = env

        self.namespaces: OrderedDict[str, Namespace] = collections.OrderedDict()

        if "KUBECONFIG" in environ and Path(environ.str("KUBECONFIG")).exists():
            config.load_kube_config(environ.str("KUBECONFIG"))
        self.kube: client.CoreV1Api = client.CoreV1Api()

        self.python = apps.PythonUtils(se=apps.PythonUtils.Sets(),
                                       li=apps.PythonUtils.Links(env=self.env))

    def is_ci_job(self) -> bool:
        return "CI_JOB_ID" in environ

    def sudo(self) -> str:
        if self.is_ci_job():
            return ""
        else:
            return "sudo"

    def chdir_to_project_root(self) -> None:
        os.chdir(str(self.env.project_root))

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

    def deploy(self) -> None:
        self.chdir_to_project_root()
        run("helm repo update")

        n: Namespace
        for n in self.namespaces.values():
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
