from pathlib import Path
import os

import plasma.apps.keycloak


class Keycloak(plasma.apps.keycloak.Keycloak):
    class Links(plasma.apps.keycloak.Keycloak.Links):
        pass

    def __init__(self, li: Links):
        super().__init__(li)
        self.app_root: Path = Path(os.path.realpath(__file__)).parent

    def deploy(self) -> None:
        super().deploy()

    def delete(self) -> None:
        super().delete()
