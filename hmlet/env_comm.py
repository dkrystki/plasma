from dataclasses import dataclass

from plasma.comm.python.pl import cluster, env
from plasma.env import Path, PlasmaEnv
import os
import plasma.aux.env_comm


@dataclass
class HmletEnvComm(cluster.ClusterEnv):
    @dataclass
    class Photos(env.BaseEnv):
        address: str = None

    @dataclass
    class Minio(env.BaseEnv):
        address: str = None

    photos: Photos = None
    minio: Photos = None
    aux: plasma.aux.env_comm.AuxEnvComm = None
    ngrok_authtoken: str = None

    def __init__(self) -> None:
        self.root = Path(os.path.realpath(__file__)).parent
        self.name = "ht"
        super().__init__()
        self.plasma = PlasmaEnv()  # monorepo env
        self.device = self.Device(k8s_ver="1.15.7", name=f"hmlet-{self.stage}")
        self.python = self.Python(poetry_ver="1.0.3",
                                  ver_major=3, ver_minor=8, ver_patch=1,
                                  pyenv_root=self.root / ".pyenv")
        self.skaffold_ver = "1.6.0"
        self.kubectl_ver = "1.17.0"
        self.helm_ver = "2.15.2"
        self.kind_ver = "0.7.0"
        self.debian_ver = "buster"
        self.docker_ver = "18.09.9"

        self.ngrok_authtoken: str = ""

    def activate(self) -> None:
        self.plasma.activate()

        super().activate()
        self._set_environ("NGROK_AUTH_TOKEN", self.ngrok_authtoken)
