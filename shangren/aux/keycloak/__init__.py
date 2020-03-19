from pathlib import Path
import os

import pl.devops


class Keycloak(pl.devops.App):
    class Links(pl.devops.App.Links):
        pass

    def __init__(self, li: Links):
        super().__init__(li)
        self.app_root: Path = Path(os.path.realpath(__file__)).parent
