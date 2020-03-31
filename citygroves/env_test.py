from plasma.env import Path

import plasma.citygroves.env_comm
import os
import subprocess

from plasma.citygroves import env_comm


class Env(plasma.citygroves.env_comm.Env):
    emoji: str = "🛠️"
    stage: str = "test"

    class Registry(env_comm.Env.Registry):
        ip: str
        address: str = "citygroves.registry.test"
        username: str = "user"
        password: str = "password"

    class Cluster(env_comm.Env.Cluster):
        ip: str = ""
        name: str = "citygroves-test"

    class Keycloak(env_comm.Env.Keycloak):
        address: str = "citygroves.keycloak.test"

    class Backend(env_comm.Env.Backend):
        address: str = "citygroves.backend.test"

    class Appgen(env_comm.Env.Appgen):
        address: str = "citygroves.appgen.test"

    class Frontend(env_comm.Env.Frontend):
        address: str = "citygroves.frontend.test"

    def __init__(self) -> None:
        super().__init__()

        self.deps_path = Path("/usr/local/bin")

        try:
            self.cluster.ip = subprocess.check_output(f"""kubectl describe nodes {self.cluster.name} | """
                                                      """grep -oP "InternalIP:  \K.*" """,  # noqa: W605
                                                      shell=True, stderr=subprocess.PIPE).decode("utf-8")
            self.cluster.ip = self.cluster.ip.strip()
        except subprocess.CalledProcessError:
            pass

        self.registry.ip = self.cluster.ip

    def activate(self) -> None:
        super().activate()
        os.environ["CG_CLUSTER_IP"] = self.cluster.ip
