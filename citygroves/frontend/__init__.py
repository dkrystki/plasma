from pathlib import Path
import os

import plasma.devops


class Frontend(plasma.devops.App):
    class Links(plasma.devops.App.Links):
        pass

    def __init__(self, li: Links):
        super().__init__("frontend", li)
        self.app_root: Path = Path(os.path.realpath(__file__)).parent

    def deploy(self) -> None:
        super().deploy()

        namespace = self.li.namespace
        stage = self.li.cluster.env.stage

        logger.info("Build image using skaffold.")
        run(f"skaffold build -p {stage}")

        logger.info("Deploy using skaffold.")
        run(f"skaffold deploy -p {stage}"
            f" --images shangren.registry.local/citygroves-{stage}/backend:latest")

    def delete(self) -> None:
        super().delete()
