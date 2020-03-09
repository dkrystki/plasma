import plasma.citygroves.frontend.env_comm
import plasma.citygroves.env_local


class Env(plasma.citygroves.frontend.env_comm.Env):
    def __init__(self) -> None:
        super().__init__()
        self.parent = plasma.citygroves.env_stage.Env()

        self.emoji = self.parent.emoji
        self.stage = self.parent.stage
