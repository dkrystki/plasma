import pl.devops


class Postgres(pl.devops.App):
    class Sets(pl.devops.App.Sets):
        pass

    class Links(pl.devops.App.Links):
        pass

    def __init__(self, se: Sets, li: Links):
        super().__init__(se, li)

    def deploy(self) -> None:
        super().deploy()
        self.li.namespace.apply_yaml("k8s/secret.yaml")
        self.li.namespace.apply_yaml("k8s/configmap.yaml")
        self.li.namespace.helm(self.se.name).install(chart="stable/postgresql", version="6.3.7")

    def delete(self) -> None:
        super().delete()

        self.li.namespace.helm(self.se.name).delete()

