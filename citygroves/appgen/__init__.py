from pathlib import Path
import os

import plasma.devops
from loguru import logger


class AppGen(plasma.devops.App):
    class Links(plasma.devops.App.Links):
        pass

    def __init__(self, li: Links):
        super().__init__("backend", li)

        self.app_root: Path = Path(os.path.realpath(__file__)).parent

    def deploy(self) -> None:
        super().deploy()

    def delete(self) -> None:
        super().delete()

