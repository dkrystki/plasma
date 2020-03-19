from pathlib import Path
import os

import pl.apps.kaniko


class Kaniko(pl.apps.kaniko.Kaniko):
    class Links(pl.apps.kaniko.Kaniko.Links):
        pass

    def __init__(self, li: Links):
        super().__init__(li)
        self.app_root: Path = Path(os.path.realpath(__file__)).parent
