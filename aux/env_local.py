import plasma.aux.env_comm


class Env(plasma.aux.env_comm.Env):
    emoji: str = "🐣"
    stage: str = "local"

    class Registry(plasma.aux.env_comm.Env.Registry):
        address = "aux.registry.local"
        username = "user"
        password = "password"

    class Cluster(plasma.aux.env_comm.Env.Cluster):
        address: str = "192.168.0.101"
        name: str = "aux-local"

    def __init__(self) -> None:
        super().__init__()
