import plasma.citygroves.backend.env_comm
import plasma.citygroves.env_local
from plasma.citygroves.env_local import CitygrovesEnv


class BackendEnv(plasma.citygroves.backend.env_comm.BackendEnvComm):
    def __init__(self) -> None:
        self.stage = "local"
        self.cluster = CitygrovesEnv()
        self.emoji = "🐣"
        self.prebuild: bool = True
        self.src_image = f"python:{self.cluster.python.ver_major}." \
                         f"{self.cluster.python.ver_minor}-slim-{self.cluster.debian_ver}"
        super().__init__()
