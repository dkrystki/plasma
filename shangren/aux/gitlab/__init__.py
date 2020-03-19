from pathlib import Path
import os

import pl.apps.gitlab


class Gitlab(pl.apps.gitlab.Gitlab):
    class Links(pl.apps.gitlab.Gitlab.Links):
        pass

    def __init__(self, li: Links):
        super().__init__(li)
        self.app_root: Path = Path(os.path.realpath(__file__)).parent
