from pathlib import Path
import os

import pl.devops


class Frontend(pl.devops.SkaffoldApp):
    class Links(pl.devops.SkaffoldApp.Links):
        pass

    def __init__(self, li: Links):
        super().__init__("frontend", li)
        self.app_root: Path = Path(os.path.realpath(__file__)).parent
