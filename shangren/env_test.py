import plasma.shangren.env_comm
import os
import subprocess


class Env(plasma.shangren.env_comm.Env):
    emoji: str = "🛠️"
    stage: str = "test"

    class Registry:
        address = "shangren.registry.test"
        username = "user"
        password = "password"

    class Cluster(plasma.shangren.env_comm.Env.Cluster):
        address: str = ""
        name: str = "shangren-test"

    def __init__(self) -> None:
        super().__init__()

    def activate(self) -> None:
        super().activate()

        try:
            self.cluster.ip = subprocess.check_output(f"""kubectl describe nodes {self.cluster.name} | """
                                                      """grep -oP "InternalIP:  \K.*" """,
                                                      shell=True, stderr=subprocess.PIPE).decode("utf-8")
            self.cluster.ip = self.cluster.ip.strip()
        except subprocess.CalledProcessError:
            pass

        os.environ["CG_CLUSTER_IP"] = self.cluster.ip
