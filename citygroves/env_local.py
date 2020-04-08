import re

import plasma.citygroves.env_comm
from aux.env_local import AuxEnv

from plasma.comm.python.pl.devops import run, CommandError


class CitygrovesEnv(plasma.citygroves.env_comm.CitygrovesEnvComm):
    def __init__(self) -> None:
        self.stage = "local"
        self.emoji = "🐣"
        super().__init__()

        self.keycloak = CitygrovesEnv.Keycloak(address="citygroves.keycloak.local")
        self.backend = CitygrovesEnv.Backend(address="citygroves.backend.local")
        self.frontend = CitygrovesEnv.Frontend(address="citygroves.frontend.local")
        self.appgen = CitygrovesEnv.Appgen(address="citygroves.appgen.local")

        self.aux = AuxEnv()

        self.registry = CitygrovesEnv.Registry(address="citygroves.registry.local",
                                               username="user",
                                               password="password")

        try:
            # TODO: Add timeout to this
            result = run(f"""kubectl describe nodes {self.device.name}""")
            ip_phrase = re.search(r"InternalIP: .*", "\n".join(result)).group(0)
            ip = ip_phrase.split(":")[1].strip()

            self.device.ip = ip
            self.registry.ip = ip

        except CommandError:
            self.device.ip = ""
