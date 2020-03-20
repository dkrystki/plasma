import pl.devops


class Redis(pl.devops.App):
    class Sets(pl.devops.App.Sets):
        pass

    class Links(pl.devops.App.Links):
        pass

    def __init__(self, se: Sets, li: Links):
        super().__init__(se, li)

    def deploy(self) -> None:
        super().deploy()
        self.li.namespace.helm(self.se.name).install(chart="stable/redis", version="9.2.0")

    def delete(self) -> None:
        super().delete()
        self.li.namespace.helm(self.se.name).delete()
