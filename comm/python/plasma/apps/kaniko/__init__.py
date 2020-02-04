from pathlib import Path
import os

import plasma.devops


class Kaniko(plasma.devops.App):
    class Links(plasma.devops.App.Links):
        pass

    def __init__(self, li: Links):
        super().__init__("kaniko", li)
        self.app_root: Path = Path(os.path.realpath(__file__)).parent

    def deploy(self) -> None:
        super().deploy()

        os.chdir(str(self.app_root))

        self.li.namespace.apply("pod.yaml")
        self.li.namespace.apply("volume.yaml")
        self.li.namespace.apply("volume-claim.yaml")

    def delete(self) -> None:
        super().delete()

        os.chdir(str(self.app_root))

        self.li.namespace.apply("pod.yaml")
        self.li.namespace.apply("volume.yaml")
        self.li.namespace.apply("volume-claim.yaml")
