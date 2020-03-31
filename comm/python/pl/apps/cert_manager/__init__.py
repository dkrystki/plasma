from dataclasses import dataclass

from pl.apps import App
from pl.devops import run


class CertManager(App):
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
        # run("kubectl apply --validate=false -f k8s/crds.yaml")
        run("kubectl apply --validate=false -f https://github.com/jetstack/cert-manager/releases/download/v0.14.0/cert-manager.crds.yaml")

        # kubectl create clusterrolebinding cluster-admin-binding --clusterrole=cluster-admin

        self.li.namespace.helm(self.se.name).install("jetstack/cert-manager", "0.14.0",
                                                     repo="jetstack https://charts.jetstack.io")
        self.li.namespace.apply_yaml("k8s/issuer.yaml")

    def delete(self) -> None:
        super().delete()

        self.li.namespace.helm(self.se.name).delete()
        self.li.namespace.delete_yaml("k8s/crds.yaml")
        self.li.namespace.delete_yaml("k8s/issuer.yaml")
