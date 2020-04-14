from hmlet.env_local import HmletEnv
from hmlet.photos.env_comm import PhotosEnvComm


class PhotosEnv(PhotosEnvComm):
    def __init__(self) -> None:
        self.stage = "local"
        self.cluster = HmletEnv()
        self.emoji = "🐣"
        self.prebuild: bool = True
        self.src_image = f"python:{self.cluster.python.ver_major}." \
                         f"{self.cluster.python.ver_minor}-slim-{self.cluster.debian_ver}"
        super().__init__()
