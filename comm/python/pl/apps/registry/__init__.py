import pl.devops


class Registry(pl.devops.App):
    class Sets(pl.devops.App.Sets):
        pass

    class Links(pl.devops.App.Links):
        pass

    def __init__(self, se: Sets, li: Links):
        super().__init__(se, li)

    def deploy(self) -> None:
        super().deploy()
        # self.li.namespace.apply_yaml("k8s/tls-secret.yaml")
        self.li.namespace.helm(self.se.name).install("stable/docker-registry", "1.9.2")

    def delete(self) -> None:
        super().delete()
        self.li.namespace.helm(self.se.name).delete()
