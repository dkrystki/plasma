from pathlib import Path
import os
from typing import Any

import plasma.env


class Env(plasma.env.Env):
    def __init__(self) -> None:
        super().__init__()

        self.app_root: Path = Path(os.path.realpath(__file__)).parent
        self.app_src: Path = self.app_root / "flesh"
        self.name: str = "frontend"
        self.parent: Any = None

    def activate(self) -> None:
        super().activate()

        os.environ["PATH"] = f"{str(self.app_root)}/.bin:{os.environ['PATH']}"
        os.environ["CG_APP_ROOT"] = str(self.app_root)
        os.environ["CG_APP_SRC"] = str(self.app_src)
