import plasma.citygroves.backend.env_comm
import plasma.citygroves.env_test


class Env(plasma.citygroves.backend.env_comm.Env, plasma.citygroves.env_test.Env):
    prebuild: bool = True

    def __init__(self) -> None:
        super().__init__()
