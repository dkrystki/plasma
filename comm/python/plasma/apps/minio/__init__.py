from pathlib import Path
import os

import plasma.devops


class Minio(plasma.devops.App):
    class Links(plasma.devops.App.Links):
        pass

    def __init__(self, li: Links):
        super().__init__("minio", li)
        self.app_root: Path = Path(os.path.realpath(__file__)).parent

    def deploy(self) -> None:
        super().deploy()
        self.li.namespace.helm("minio").install("stable/minio", "5.0.12")

    def delete(self) -> None:
        super().delete()

        self.li.namespace.helm("minio").delete()
