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

        plasma.devops.run("helm repo add codecentric https://codecentric.github.io/helm-charts")
        self.li.namespace.helm("keycloak").install("codecentric/keycloak", "7.2.0")

    def delete(self) -> None:
        super().delete()

        self.li.namespace.helm("keycloak").delete()
