import re

from plasma.hmlet.env_comm import HmletEnvComm
from aux.env_local import AuxEnv

from plasma.comm.python.pl.devops import run, CommandError


class HmletEnv(HmletEnvComm):
    def __init__(self) -> None:
        self.stage = "test"
        self.emoji = "🛠"
        super().__init__()

        self.photos = HmletEnv.Photos(address="hmlet.photos.test")
        self.minio = HmletEnv.Minio(address="hmlet.minio.test")

        self.aux = AuxEnv()  # Auxiliary cluster's registry is used for caching

        self.registry = HmletEnv.Registry(address="hmlet.registry.test",
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
            self.registry.ip = ""
