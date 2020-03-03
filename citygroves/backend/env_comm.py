from pathlib import Path
import os

import citygroves.env_comm


class Env(citygroves.env_comm.Env):
    def __init__(self) -> None:
        super().__init__()

        self.app_root: Path = Path(os.path.realpath(__file__)).parent
        self.app_src: Path = self.app_root / "flesh"
        self.name: str = "backend"
        self.parent = None

    def activate(self) -> None:
        super().activate()

        self.project_root = Path(os.path.realpath(__file__)).parent

        os.environ["PATH"] = f"{str(self.app_root)}/.bin:{os.environ['PATH']}"
        os.environ["CG_APP_ROOT"] = str(self.app_root)
        os.environ["CG_APP_SRC"] = str(self.app_src)

