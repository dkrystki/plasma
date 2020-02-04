from pathlib import Path
import os

import plasma.devops


class Keycloak(plasma.devops.App):
    class Links(plasma.devops.App.Links):
        pass

    def __init__(self, li: Links):
        super().__init__(li)
        self.app_root: Path = Path(os.path.realpath(__file__)).parent
