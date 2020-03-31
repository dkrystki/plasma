from dataclasses import dataclass

from pl.apps import App


class Ingress(App):
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
        self.li.namespace.helm(self.se.name).install("stable/nginx-ingress", "1.34.2")

        # Kind needs it
        self.li.namespace.kubectl(
            """patch deployments ingress-controller -p '{"spec":{"template":{"spec":{"containers":["""
            """{"name":"nginx-ingress-controller","ports":[{"containerPort":80,"hostPort":80},"""
            """{"containerPort":443,"hostPort":443}]}]}}}}'""")

    def delete(self) -> None:
        super().delete()

        self.li.namespace.helm(self.se.name).delete()
