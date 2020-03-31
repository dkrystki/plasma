from dataclasses import dataclass

from pl.apps import App


class Redis(App):
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
        self.li.namespace.helm(self.se.name).install(chart="stable/redis", version="9.2.0")

    def delete(self) -> None:
        super().delete()
        self.li.namespace.helm(self.se.name).delete()
