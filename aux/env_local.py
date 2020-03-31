import plasma.aux.env_comm
import subprocess


class Env(plasma.aux.env_comm.Env):
    emoji: str = "🐣"
    stage: str = "local"

    class Registry(plasma.aux.env_comm.Env.Registry):
        ip: str
        address: str = "aux.registry.local"
        username: str = "user"
        password: str = "password"

    class Cluster(plasma.aux.env_comm.Env.Cluster):
        ip: str
        name: str = "aux-local"

    class Graylog(plasma.aux.env_comm.Env.Graylog):
        address: str = "aux.graylog.local"

    class Sentry(plasma.aux.env_comm.Env.Sentry):
        address: str = "aux.sentry.local"

    def __init__(self) -> None:
        super().__init__()

        ip: str = subprocess.check_output("hostname -I", shell=True).split()[0].decode("utf-8")

        self.cluster.ip = ip
        self.registry.ip = ip
