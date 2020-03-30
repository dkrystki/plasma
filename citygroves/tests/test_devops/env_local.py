import plasma.citygroves.env_comm


class Env(plasma.citygroves.env_comm.Env):
    emoji: str = "🐣"
    stage: str = "local"

    class Registry(plasma.citygroves.env_comm.Env.Registry):
        ip = "127.0.0.1"
        address = "citygroves.registry.local"
        username = "user"
        password = "password"

    class Cluster(plasma.citygroves.env_comm.Env.Cluster):
        address: str = ""
        name: str = "citygroves-local"

    def __init__(self) -> None:
        super().__init__()

