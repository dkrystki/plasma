import plasma.citygroves.frontend.env_comm
import plasma.citygroves.env_local
from plasma.citygroves.env_local import CitygrovesEnv


class FrontendEnv(plasma.citygroves.frontend.env_comm.FrontendEnvComm):
    def __init__(self) -> None:
        self.stage = "local"
        self.cluster = CitygrovesEnv()
        self.emoji = "🐣"
        self.prebuild: bool = True
        self.src_image = "node:13.5.0-stretch-slim"
        super().__init__()
