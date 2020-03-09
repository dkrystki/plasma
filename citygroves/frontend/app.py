from pathlib import Path
import os

import pl.devops
from loguru import logger
from pl.devops import run


class Frontend(pl.devops.App):
    class Links(pl.devops.App.Links):
        pass

    def __init__(self, li: Links):
        super().__init__("frontend", li)
        self.app_root: Path = Path(os.path.realpath(__file__)).parent

    def deploy(self) -> None:
        super().deploy()

        namespace = self.li.namespace
        stage = self.li.cluster.env.stage

        logger.info("Build image using skaffold.")
        run(f"skaffold build -p {stage}", print_output=True)

        logger.info("Deploy using skaffold.")
        run(f"skaffold deploy -p {stage}"
            f" --images shangren.registry.local/citygroves-{stage}/frontend:latest", print_output=True)

    def delete(self) -> None:
        super().delete()

    def skaffold(self) -> None:
        run(f"skaffold dev -p {self.li.cluster.env.stage}", print_output=True)
