import plasma.citygroves.env_comm


class Env(plasma.citygroves.env_comm.Env):
    emoji: str = "🤖"
    stage: str = "prod"

    class Registry(plasma.citygroves.env_comm.Env.Registry):
        ip = "127.0.0.1"
        address = "citygroves.registry.prod"
        username = "user"
        password = "password"

    class Cluster(plasma.citygroves.env_comm.Env.Cluster):
        address: str = ""
        name: str = "citygroves-prod"

    def __init__(self) -> None:
        super().__init__()

