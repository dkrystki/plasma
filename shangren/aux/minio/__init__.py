from pathlib import Path
import os

import pl.apps.minio


class Minio(pl.apps.minio.Minio):
    class Links(pl.apps.minio.Minio.Links):
        pass

    def __init__(self, li: Links):
        super().__init__(li)
        self.app_root: Path = Path(os.path.realpath(__file__)).parent
