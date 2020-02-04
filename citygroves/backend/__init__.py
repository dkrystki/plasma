from pathlib import Path
import os

import plasma.devops
from loguru import logger
from plasma.devops import Cluster, Namespace, run


class Backend(plasma.devops.App):
    class Links(plasma.devops.App.Links):
        cluster: Cluster
        namespace: Namespace

    def __init__(self, li: Links):
        super().__init__("backend", li)

        self.app_root: Path = Path(os.path.realpath(__file__)).parent

    def deploy(self) -> None:
        super().deploy()

        namespace = self.li.namespace
        stage = self.li.cluster.env.stage

        logger.info("🚀Creating sql database.")
        postgres_pod: str = next(pod for pod in namespace.get_pods() if "postgres" in pod)

        namespace.wait_for_pod(postgres_pod)

        namespace.copy("sql/init.sql", f"{postgres_pod}:/tmp/init.sql")
        namespace.exec(postgres_pod, "PGUSER=postgres PGPASSWORD=password psql -a -f /tmp/init.sql")
        logger.info("👌Created sql database.")

        logger.info("Build image using skaffold.")
        run(f"skaffold build -p {stage}")

        logger.info("Deploy using skaffold.")
        run(f"skaffold deploy -p {stage}"
            f" --images shangren.registry.local/citygroves-{stage}/backend:latest")

    def delete(self) -> None:
        super().delete()
