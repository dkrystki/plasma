import pl.devops


class CertManager(pl.devops.App):
    class Sets(pl.devops.App.Sets):
        pass

    class Links(pl.devops.App.Links):
        pass

    def __init__(self, se: Sets, li: Links):
        super().__init__(se, li)

    def deploy(self) -> None:
        super().deploy()
        # pl.devops.run("kubectl apply --validate=false -f k8s/crds.yaml")
        pl.devops.run("kubectl apply --validate=false -f https://github.com/jetstack/cert-manager/releases/download/v0.14.0/cert-manager.crds.yaml")

        # kubectl create clusterrolebinding cluster-admin-binding --clusterrole=cluster-admin

        self.li.namespace.helm(self.se.name).install("jetstack/cert-manager", "0.14.0",
                                                     repo="jetstack https://charts.jetstack.io")
        self.li.namespace.apply_yaml("k8s/issuer.yaml")

    def delete(self) -> None:
        super().delete()

        self.li.namespace.helm(self.se.name).delete()
        self.li.namespace.delete_yaml("k8s/crds.yaml")
        self.li.namespace.delete_yaml("k8s/issuer.yaml")
