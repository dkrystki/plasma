import plasma.citygroves.env_comm


class Env(plasma.citygroves.env_comm.Env):
    emoji: str = "🤖"
    stage: str = "stage"

    class Registry(plasma.citygroves.env_comm.Env.Registry):
        ip = "127.0.0.1"
        address = "citygroves.registry.stage"
        username = "user"
        password = "password"

    class Cluster(plasma.citygroves.env_comm.Env.Cluster):
        address: str = ""
        name: str = "citygroves-stage"

    def __init__(self) -> None:
        super().__init__()

