import plasma.citygroves.appgen.env_comm
import plasma.citygroves.env_test


class Env(plasma.citygroves.appgen.env_comm.Env):
    def __init__(self) -> None:
        super().__init__()
        self.parent = plasma.citygroves.env_test.Env()

        self.emoji = self.parent.emoji
        self.stage = self.parent.stage
