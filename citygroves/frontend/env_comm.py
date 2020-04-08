from plasma.comm.python.pl.apps import AppEnv
from plasma.env import Path
import os


class FrontendEnvComm(AppEnv):
    helm_release_name: str = None
    app_name: str = None
    prebuild: bool = None

    def __init__(self) -> None:
        self.root = Path(os.path.realpath(__file__)).parent
        self.python = self.cluster.python

        self.name: str = "fe"
        self.app_name = "frontend"

        super().__init__()

        self.helm_release_name = "citygroves-frontend"

        self.dockerfile_templ = self.cluster.comm / "docker/Dockerfile.node.templ"
