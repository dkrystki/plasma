from pathlib import Path
import os
from tempfile import NamedTemporaryFile
from typing import Dict, Any, List


class Tele:
    def __init__(self, env) -> None:
        pass

    def shell(self) -> None:
        self.activate()

        with NamedTemporaryFile(mode='w+', buffering=True, delete=True) as tmprc:
            tmprc.write('source ~/.bashrc\n')
            # that's the only way to modify the prompt
            tmprc.write(self.as_string())
            tmprc.write(f'PS1={self.emoji}\({self.name}\)$PS1\n')

            os.system(f"bash --rcfile {tmprc.name}")
