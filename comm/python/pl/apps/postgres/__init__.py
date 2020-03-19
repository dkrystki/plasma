from pathlib import Path
import os

import pl.devops


class Postgres(pl.devops.App):
    class Links(pl.devops.App.Links):
        pass

    def __init__(self, li: Links):
        super().__init__("postgres", li)
        self.app_root: Path = Path(os.path.realpath(__file__)).parent

    def deploy(self) -> None:
        super().deploy()
        self.li.namespace.apply("secret.yaml")
        self.li.namespace.apply("configmap.yaml")
        self.li.namespace.helm("postgresql").install(chart="stable/postgresql", version="6.3.7")

    def delete(self) -> None:
        super().delete()

        self.li.namespace.helm("postgresql").delete()

