from plasma.comm.python.pl.apps import AppEnv
from plasma.env import Path
import os


class PhotosEnvComm(AppEnv):
    helm_release_name: str = None
    app_name: str = None
    prebuild: bool = None

    def __init__(self) -> None:
        self.root = Path(os.path.realpath(__file__)).parent
        self.python = self.cluster.python
        self.name: str = "ps"
        self.app_name = "photos"

        super().__init__()
        self.helm_release_name = "hmlet-photos"

        self.dockerfile_templ = self.cluster.comm / "docker/Dockerfile.python.templ"
