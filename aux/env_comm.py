from dataclasses import dataclass, fields
from pathlib import Path
import os

from plasma.comm.python.pl import cluster, env
from plasma.env import PlasmaEnv


@dataclass
class AuxEnvComm(cluster.ClusterEnv):
    @dataclass
    class Graylog(env.BaseEnv):
        address: str = None

    @dataclass
    class Sentry(env.BaseEnv):
        address: str = None

    graylog: Graylog = None
    sentry: Sentry = None

    def __init__(self) -> None:
        self.root = Path(os.path.realpath(__file__)).parent
        self.name = "au"
        super().__init__()

        self.device = self.Device(k8s_ver="1.15")
        self.skaffold_ver = "1.6.0"
        self.kubectl_ver = "1.17.0"
        self.helm_ver = "2.15.2"
        self.kind_ver = "0.7.0"
        self.debian_ver = "buster"
        self.docker_ver = "18.09.9"
        self.python = self.Python(poetry_ver="1.0.3",
                                  ver_major=3, ver_minor=8, ver_patch=1,
                                  pyenv_root=self.root / ".pyenv")
        self.plasma = PlasmaEnv()
