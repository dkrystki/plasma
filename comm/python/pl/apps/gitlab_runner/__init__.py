from dataclasses import dataclass

from pl.apps import App
from pl.devops import run


class GitlabRunner(App):
    @dataclass
    class Sets(App.Sets):
        pass

    @dataclass
    class Links(App.Links):
        pass

    def __init__(self, se: Sets, li: Links):
        super().__init__(se, li)
        self.runner = self.li.namespace.helm(self.se.name)

    def deploy(self) -> None:
        super().deploy()

        run("helm repo add gitlab https://charts.gitlab.io")
        self.runner.install(chart="gitlab/gitlab-runner", version="0.12.0")

    def delete(self) -> None:
        super().delete()

        self.runner.delete()
