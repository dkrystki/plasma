from dataclasses import dataclass
from pathlib import Path
import os

from pl.apps import App


class Minio(App):
    @dataclass
    class Sets(App.Sets):
        pass

    @dataclass
    class Links(App.Links):
        pass

    def __init__(self, se: Sets, li: Links):
        super().__init__(se, li)

    def deploy(self) -> None:
        super().deploy()
        self.li.namespace.helm(self.se.name).install("stable/minio", "5.0.12")

    def delete(self) -> None:
        super().delete()

        self.li.namespace.helm(self.se.name).delete()
