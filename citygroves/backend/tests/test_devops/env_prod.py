import plasma.citygroves.backend.env_comm
import plasma.citygroves.tests.test_devops.env_prod


class Env(plasma.citygroves.backend.env_comm.Env, plasma.citygroves.tests.test_devops.env_prod.Env):
    def __init__(self) -> None:
        super().__init__()
