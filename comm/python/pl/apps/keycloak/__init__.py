import pl.devops


class Keycloak(pl.devops.App):
    class Sets(pl.devops.App.Sets):
        pass

    class Links(pl.devops.App.Links):
        pass

    def __init__(self, se: Sets, li: Links):
        super().__init__(se, li)

    def deploy(self) -> None:
        super().deploy()

        pl.devops.run("helm repo add codecentric https://codecentric.github.io/helm-charts")
        self.li.namespace.helm(self.se.name).install("codecentric/keycloak", "7.2.0")

    def delete(self) -> None:
        super().delete()

        self.li.namespace.helm(self.se.name).delete()
