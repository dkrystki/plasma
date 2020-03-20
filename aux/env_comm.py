from pathlib import Path
import os
import plasma.env


class Env(plasma.env.Env):
    project_code: str = "AU"
    project_name: str = "aux"
    project_root: Path
    emoji: str
    stage: str
    kubeconfig: str
    poetry_ver: str = "1.0.3"
    python_ver_major: int = 3
    python_ver_minor: int = 8
    python_ver_patch: int = 1
    skaffold_ver: str = "1.6.0"
    kubectl_ver: str = "1.17.0"
    helm_ver: str = "2.15.2"
    debian_ver: str = "buster"
    docker_ver: str = "18.09.9"
    bin_path: Path = Path(".bin")
    ngrok_authtoken: str = ""

    class Cluster:
        address: str = ""
        name: str = ""
        kubernetes_ver: str = "1.15"

    class Registry:
        address: str
        username: str
        password: str

    def __init__(self) -> None:
        super().__init__()
        self.project_root = Path(os.path.realpath(__file__)).parent
        self.name: str = "aux"

    def activate(self) -> None:
        super().activate()
