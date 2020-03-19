import plasma.citygroves.backend.env_comm
import plasma.citygroves.env_local


class Env(plasma.citygroves.backend.env_comm.Env):
    def __init__(self) -> None:
        super().__init__()
        self.parent = plasma.citygroves.env_local.Env()

        self.emoji = self.parent.emoji
        self.stage = self.parent.stage
