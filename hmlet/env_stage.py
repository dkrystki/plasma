from plasma.hmlet.env_comm import HmletEnvComm

# Normaly this file shouldn not be committed


class HmletEnv(HmletEnvComm):
    def __init__(self) -> None:
        self.stage = "stage"
        self.emoji = "🤖"
        super().__init__()

        self.photos = HmletEnv.Photos(address="hmlet.photos.stage")
        self.minio = HmletEnv.Minio(address="hmlet.minio.stage")

        self.registry = HmletEnv.Registry(address="hmlet.registry.stage",
                                          username="user",
                                          password="password")
        self.device.ip = "52.76.215.230"
