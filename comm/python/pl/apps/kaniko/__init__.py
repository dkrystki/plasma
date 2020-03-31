from dataclasses import dataclass

from pl.apps import App


class Kaniko(App):
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

        self.li.namespace.apply_yaml("k8s/pod.yaml")
        self.li.namespace.apply_yaml("k8s/volume.yaml")
        self.li.namespace.apply_yaml("k8s/volume-claim.yaml")

    def delete(self) -> None:
        super().delete()

        self.li.namespace.delete_yaml("k8s/pod.yaml")
        self.li.namespace.delete_yaml("k8s/volume.yaml")
        self.li.namespace.delete_yaml("k8s/volume-claim.yaml")
