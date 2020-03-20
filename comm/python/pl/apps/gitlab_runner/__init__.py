import pl.devops


class GitlabRunner(pl.devops.App):
    class Sets(pl.devops.App.Sets):
        pass

    class Links(pl.devops.App.Links):
        pass

    def __init__(self, se: Sets, li: Links):
        super().__init__(se, li)
        self.runner = self.li.namespace.helm(self.se.name)

    def deploy(self) -> None:
        super().deploy()

        pl.devops.run("helm repo add gitlab https://charts.gitlab.io")
        self.runner.install(chart="gitlab/gitlab-runner", version="0.12.0")

    def delete(self) -> None:
        super().delete()

        self.runner.delete()
