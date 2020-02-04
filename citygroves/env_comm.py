#!../.venv/bin/python
from pathlib import Path
import os
import plasma.shell


class Env(plasma.shell.Env):
    project_code: str = "CG"
    emoji: str
    stage: str
    kubeconfig: str
    poetry_ver: str = "1.0.3"
    python_ver_major: int = 3
    python_ver_minor: int = 8
    python_ver_patch: int = 1
    skaffold_ver: str = "1.3.1"
    kubectl_ver: str = "1.17.0"
    helm_ver: str = "2.15.2"
    debian_ver: str = "buster"
    docker_ver: str = "18.09.9"
    cluster_address: str = "192.168.0.5"
    registry_address: str = "shangren.registry.local"

    def __init__(self) -> None:
        super().__init__()

        self.project_root = Path()
        self.name: str = "citygroves"
        self.stage: str = self.__class__.__name__.lower()
        self.namespace_name: str = f"citygroves-{self.stage}"

    def activate(self) -> None:
        super().activate()

        self.project_root = Path(os.path.realpath(__file__)).parent

        os.environ["PATH"] = f"{str(self.project_root)}/.bin:{os.environ['PATH']}"
        os.environ["CG_PROJECT_ROOT"] = str(self.project_root)
        os.environ["CG_PROJECT_CODE"] = self.project_code
        os.environ["CG_STAGE"] = self.stage
        os.environ["CG_STAGE_EMOJI"] = self.emoji
        os.environ["KUBECONFIG"] = str(self.project_root / f"envs/{self.stage}/kubeconfig.yaml")
        os.environ["CG_POETRY_VER"] = str(self.poetry_ver)
        os.environ["CG_PYTHON_VER_MAJOR"] = str(self.python_ver_major)
        os.environ["CG_PYTHON_VER_MINOR"] = str(self.python_ver_minor)
        os.environ["CG_PYTHON_VER_PATCH"] = str(self.python_ver_patch)
        os.environ["CG_PYTHON_VER"] = f"{self.python_ver_major}.{self.python_ver_minor}.{self.python_ver_patch}"
        os.environ["CG_DEBIAN_VER"] = self.debian_ver
        os.environ["CG_SKAFFOLD_VER"] = self.skaffold_ver
        os.environ["CG_KUBECTL_VER"] = self.kubectl_ver
        os.environ["CG_HELM_VER"] = self.helm_ver
        os.environ["CG_DOCKER_VER"] = self.docker_ver
        os.environ["CG_CLUSTER_ADDRESS"] = self.cluster_address
        os.environ["CG_REGISTRY_ADDRESS"] = self.registry_address
        os.environ["CG_APP_NAMESPACE"] = self.namespace_name
        os.environ["PLASMA_DEBUG"] = "False"
