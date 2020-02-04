from pathlib import Path
import os

import plasma.apps.kaniko


class Kaniko(plasma.apps.kaniko.Kaniko):
    class Links(plasma.apps.kaniko.Kaniko.Links):
        pass

    def __init__(self, li: Links):
        super().__init__(li)
        self.app_root: Path = Path(os.path.realpath(__file__)).parent
