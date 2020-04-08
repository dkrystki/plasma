import re

import plasma.citygroves.env_comm
from plasma.comm.python.pl.env import Path

from plasma.comm.python.pl.devops import run, CommandError
from plasma.aux.env_local import AuxEnv


class CitygrovesEnv(plasma.citygroves.env_comm.CitygrovesEnvComm):
    def __init__(self) -> None:
        self.stage = "test"
        self.emoji = "🛠"
        super().__init__()
        self.registry = CitygrovesEnv.Registry(address="citygroves.registry.test",
                                               username="user",
                                               password="password")

        self.keycloak = CitygrovesEnv.Keycloak(address="citygroves.keycloak.test")
        self.backend = CitygrovesEnv.Backend(address="citygroves.backend.test")
        self.frontend = CitygrovesEnv.Frontend(address="citygroves.frontend.test")
        self.appgen = CitygrovesEnv.Appgen(address="citygroves.appgen.test")

        self.aux = AuxEnv()

        self.deps_path = Path("/usr/local/bin")

        try:
            result = run(f"""kubectl describe nodes {self.device.name}""")
            ip_phrase = re.search(r"InternalIP: .*", "\n".join(result)).group(0)
            ip = ip_phrase.split(":")[1].strip()

            self.device.ip = ip
            self.registry.ip = ip

        except CommandError:
            self.device.ip = ""
            self.registry.ip = ""
