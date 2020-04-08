import os
from dataclasses import dataclass

from plasma.comm.python.pl.env import Env, Path


@dataclass
class PlasmaEnv(Env):
    def __init__(self) -> None:
        self.root = Path(os.path.realpath(__file__)).parent
        self.stage = "local"
        self.name = "pl"

        super().__init__()

        self.emoji = ""
        self.python = Env.Python(poetry_ver="1.0.3",
                                 ver_major=3, ver_minor=8, ver_patch=1,
                                 pyenv_root=self.root / ".pyenv")
