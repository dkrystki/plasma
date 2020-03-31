from dataclasses import dataclass

from pl.apps import App

from pl.kube import Pod


class Postgres(App):
    @dataclass
    class Sets(App.Sets):
        pass

    @dataclass
    class Links(App.Links):
        pass

    def __init__(self, se: Sets, li: Links):
        super().__init__(se, li)
        self.release = self.li.namespace.helm(self.se.name)

        self.master = Pod(
            se=Pod.Sets(name=self.se.name + "-0"),
            li=Pod.Links(self)
        )

    def deploy(self) -> None:
        super().deploy()
        self.li.namespace.apply_yaml("k8s/secret.yaml")
        self.li.namespace.apply_yaml("k8s/configmap.yaml")
        self.release.install(chart="stable/postgresql", version="6.3.7")

    def delete(self) -> None:
        super().delete()

        self.release.delete()
