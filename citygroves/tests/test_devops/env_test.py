import plasma.citygroves.env_comm


class Env(plasma.citygroves.env_comm.Env):
    emoji: str = "🛠️"
    stage: str = "test"

    class Registry(plasma.citygroves.env_comm.Env.Registry):
        ip = "127.0.0.1"
        address = "citygroves.registry.test"
        username = "user"
        password = "password"

    class Cluster(plasma.citygroves.env_comm.Env.Cluster):
        address: str = ""
        name: str = "citygroves-test"

    def __init__(self) -> None:
        super().__init__()
