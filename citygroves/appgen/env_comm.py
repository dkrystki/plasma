from plasma.comm.python.pl.apps import AppEnv
from plasma.env import Path
import os


class AppgenEnvComm(AppEnv):
    helm_release_name: str = None
    app_name: str = None
    prebuild: bool = None

    def __init__(self) -> None:
        self.root = Path(os.path.realpath(__file__)).parent
        self.python = self.cluster.python
        self.name: str = "ag"
        self.app_name = "appgen"

        super().__init__()
        self.helm_release_name = "citygroves-appgen"

        self.dockerfile_templ = self.cluster.comm / "docker/Dockerfile.python.templ"
