from plasma.hmlet.env_stage import HmletEnv
from plasma.hmlet.photos.env_comm import PhotosEnvComm


class PhotosEnv(PhotosEnvComm):
    def __init__(self) -> None:
        self.cluster = HmletEnv()
        self.stage = self.cluster.stage
        self.emoji = self.cluster.emoji
        self.prebuild: bool = True
        self.src_image = f"python:{self.cluster.python.ver_major}." \
                         f"{self.cluster.python.ver_minor}-slim-{self.cluster.debian_ver}"
        super().__init__()

        self.minio = PhotosEnvComm.Minio(
            endpoint="minio.aux",
            public_endpoint="http://hmlet.minio.stage",
            access_key="AccessKey",
            secret_key="SecretKey",
            media_bucket_name="media",
            static_bucket_name="static"
        )
