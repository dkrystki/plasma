import plasma.citygroves.appgen.env_comm
import plasma.citygroves.env_test


class Env(plasma.citygroves.appgen.env_comm.Env, plasma.citygroves.env_test.Env):
    def __init__(self) -> None:
        super().__init__()
