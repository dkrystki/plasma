#!../.venv/bin/python
from pathlib import Path
import os
import plasma.env


class Env(plasma.env.Env):
    project_code: str = "SG"
    emoji: str
    stage: str
    kubeconfig: str
    python_ver_major: int = 3
    python_ver_minor: int = 8
    python_ver_patch: int = 1
    skaffold_ver: str = "1.3.1"
    kubectl_ver: str = "1.17.0"
    helm_ver: str = "2.15.2"
    debian_ver: str = "buster"
    docker_ver: str = "18.09.9"

    def __init__(self) -> None:
        super().__init__()

        self.project_root = Path()
        self.name: str = "shangren"
        self.stage: str = self.__class__.__name__.lower()

    def activate(self) -> None:
        super().activate()

        self.project_root = Path(os.path.realpath(__file__)).parent

        os.environ["PATH"] = f"{str(self.project_root)}/.bin:{os.environ['PATH']}"
        os.environ["SG_PROJECT_ROOT"] = str(self.project_root)
        os.environ["SG_PROJECT_CODE"] = self.project_code
        os.environ["SG_STAGE"] = self.stage
        os.environ["SG_STAGE_EMOJI"] = self.emoji
        os.environ["KUBECONFIG"] = str(self.project_root / f"envs/{self.stage}/kubeconfig.yaml")
        os.environ["SG_PYTHON_VER_MAJOR"] = str(self.python_ver_major)
        os.environ["SG_PYTHON_VER_MINOR"] = str(self.python_ver_minor)
        os.environ["SG_PYTHON_VER_PATCH"] = str(self.python_ver_patch)
        os.environ["SG_PYTHON_VER"] = f"{self.python_ver_major}.{self.python_ver_minor}.{self.python_ver_patch}"
        os.environ["SG_DEBIAN_VER"] = self.debian_ver
        os.environ["SG_SKAFFOLD_VER"] = self.skaffold_ver
        os.environ["SG_KUBECTL_VER"] = self.kubectl_ver
        os.environ["SG_HELM_VER"] = self.helm_ver
        os.environ["SG_DOCKER_VER"] = self.docker_ver
        os.environ["PLASMA_DEBUG"] = "False"
