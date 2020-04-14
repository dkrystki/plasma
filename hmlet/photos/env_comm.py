from dataclasses import dataclass
from typing import Optional

from plasma.comm.python.pl.apps import AppEnv
from plasma.comm.python.pl.env import BaseEnv
from plasma.env import Path
import os


@dataclass
class PhotosEnvComm(AppEnv):
    @dataclass
    class Minio(BaseEnv):
        endpoint: str = None
        access_key: str = None
        secret_key: str = None
        media_bucket_name: str = None
        static_bucket_name: str = None

    helm_release_name: str = None
    app_name: str = None
    prebuild: bool = None
    minio: Minio = None

    def __init__(self) -> None:
        self.root = Path(os.path.realpath(__file__)).parent
        self.python = self.cluster.python
        self.name: str = "ps"
        self.app_name = "photos"

        super().__init__()
        self.helm_release_name = "hmlet-photos"

        self.dockerfile_templ = self.cluster.comm / "docker/Dockerfile.python.templ"

    def activate(self) -> None:
        super().activate()

        self._set_environ("MINIO_STORAGE_ENDPOINT", self.minio.endpoint)
        self._set_environ("MINIO_STORAGE_ACCESS_KEY", self.minio.access_key)
        self._set_environ("MINIO_STORAGE_SECRET_KEY", self.minio.secret_key)
        self._set_environ("MINIO_STORAGE_MEDIA_BUCKET_NAME", self.minio.media_bucket_name)
        self._set_environ("MINIO_STORAGE_STATIC_BUCKET_NAME", self.minio.static_bucket_name)

        os.environ["PATH"] = f"{str(self.src)}/.venv/bin:{os.environ['PATH']}"
