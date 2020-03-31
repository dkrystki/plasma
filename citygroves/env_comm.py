from importlib import import_module
from plasma.env import Path
import os
import plasma.aux.env_comm


class Env(plasma.env.Env):
    name: str = "cg"
    project_code: str = "CG"
    project_name: str = "citygroves"
    app_name = "citygroves"
    app_root: Path
    project_root: Path
    project_comm: Path
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
    kind_ver: str = "0.7.0"
    debian_ver: str = "buster"
    docker_ver: str = "18.09.9"
    bin_path: Path = Path(".bin")
    ngrok_authtoken: str = ""

    aux: plasma.aux.env_comm.Env

    class Cluster:
        ip: str = ""
        name: str = ""
        kubernetes_ver: str = "1.15.7"

    class Registry:
        address: str
        username: str
        password: str

    class Keycloak:
        address: str

    class Backend:
        address: str

    class Appgen:
        address: str

    class Frontend:
        address: str

    def __init__(self) -> None:
        super().__init__()

        self.project_root = Path(os.path.realpath(__file__)).parent
        self.app_root = self.project_root

        self.deps_path = self.project_root / Path(".deps")

        self.project_comm = self.project_root / "comm"

        if self.stage in ["local", "test"]:
            self.aux = import_module(f"plasma.aux.env_local").Env()

        self.registry = self.__class__.Registry()
        self.keycloak = self.__class__.Keycloak()
        self.backend = self.__class__.Backend()
        self.appgen = self.__class__.Appgen()
        self.frontend = self.__class__.Frontend()

    def activate(self) -> None:
        super().activate()
        os.environ["CG_NGROK_AUTH_TOKEN"] = self.ngrok_authtoken
