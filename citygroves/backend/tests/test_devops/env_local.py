import plasma.citygroves.backend.env_comm
import plasma.citygroves.tests.test_devops.env_local


class Env(plasma.citygroves.backend.env_comm.Env, plasma.citygroves.tests.test_devops.env_local.Env):
    def __init__(self) -> None:
        super().__init__()
