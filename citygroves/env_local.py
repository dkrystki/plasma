import plasma.citygroves.env_comm
import os
import subprocess


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

    def activate(self) -> None:
        super().activate()

        try:
            self.cluster.address = subprocess.check_output(f"""kubectl describe nodes {self.cluster.name} | """
                                                      """grep -oP "InternalIP:  \K.*" """,
                                                      shell=True, stderr=subprocess.PIPE).decode("utf-8")
            self.cluster.address = self.cluster.address.strip()
        except subprocess.CalledProcessError:
            pass
