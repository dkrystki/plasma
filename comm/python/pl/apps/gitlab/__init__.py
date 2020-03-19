from pathlib import Path
import os

from pl.devops import App, run


class Gitlab(App):
    class Links(App.Links):
        pass

    def __init__(self, li: Links):
        super().__init__("gitlab", li)
        self.app_root: Path = Path(os.path.realpath(__file__)).parent
        self.runner = self.li.namespace.helm("runner")

    def deploy(self) -> None:
        super().deploy()

        run("helm repo add gitlab https://charts.gitlab.io")
        self.runner.install(chart="gitlab/gitlab-runner", version="0.12.0")

    def delete(self) -> None:
        super().delete()

        self.runner.delete()
