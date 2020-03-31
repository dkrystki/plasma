import plasma.citygroves.frontend.env_comm
import plasma.citygroves.env_local


class Env(plasma.citygroves.frontend.env_comm.Env, plasma.citygroves.env_local.Env):
    def __init__(self) -> None:
        super().__init__()
