import plasma.citygroves.backend.env_comm
import plasma.citygroves.env_stage


class Env(plasma.citygroves.backend.env_comm.Env, plasma.citygroves.env_stage.Env):
    def __init__(self) -> None:
        super().__init__()
