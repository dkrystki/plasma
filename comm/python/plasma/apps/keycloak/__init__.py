from pathlib import Path
import os

import plasma.devops


class Keycloak(plasma.devops.App):
    class Links(plasma.devops.App.Links):
        pass

    def __init__(self, li: Links):
        super().__init__("keycloak", li)
        self.app_root: Path = Path(os.path.realpath(__file__)).parent

    def deploy(self) -> None:
        super().deploy()

        self.li.namespace.helm("keycloak").install("stable/fluent-bit", "2.8.2")

    def delete(self) -> None:
        super().delete()

        self.li.namespace.helm("keycloak").delete()
