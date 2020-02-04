from pathlib import Path
import os

import plasma.apps.minio


class Minio(plasma.apps.minio.Minio):
    class Links(plasma.apps.minio.Minio.Links):
        pass

    def __init__(self, li: Links):
        super().__init__(li)
        self.app_root: Path = Path(os.path.realpath(__file__)).parent
