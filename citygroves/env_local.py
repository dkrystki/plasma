import plasma.citygroves.env_comm
import os
import subprocess

from plasma.citygroves import env_comm
from plasma.aux.env_local import Env as AuxEnv


class Env(plasma.citygroves.env_comm.Env):
    emoji: str = "🐣"
    stage: str = "local"

    class Registry(env_comm.Env.Registry):
        ip: str
        address: str = "aux.registry.local"
        username: str = "user"
        password: str = "password"

    class Cluster(env_comm.Env.Cluster):
        ip: str = ""
        name: str = "citygroves-local"

    class Keycloak(env_comm.Env.Keycloak):
        address: str = "citygroves.keycloak.local"

    class Backend(env_comm.Env.Backend):
        address: str = "citygroves.backend.local"

    class Appgen(env_comm.Env.Appgen):
        address: str = "citygroves.appgen.local"

    class Frontend(env_comm.Env.Frontend):
        address: str = "citygroves.frontend.local"

    def __init__(self) -> None:
        super().__init__()

        try:
            self.cluster.ip = subprocess.check_output(f"""kubectl describe nodes {self.cluster.name} | """
                                                      """grep -oP "InternalIP:  \K.*" """,  # noqa: W605
                                                      shell=True, stderr=subprocess.PIPE).decode("utf-8")
            self.cluster.ip = self.cluster.ip.strip()
        except subprocess.CalledProcessError:
            pass

        aux_env = AuxEnv()
        self.registry.ip = aux_env.registry.ip

    def activate(self) -> None:
        super().activate()
        os.environ["CG_CLUSTER_IP"] = self.cluster.ip
