from pathlib import Path
import os

from loguru import logger

from shang.utils.deploy import kube, Namespace


def deploy() -> None:
    os.chdir(Path(__file__).absolute().parent)
    logger.info("🚀Deploying bitstamp.")

    logger.info("🚀Creating sql database.")
    postgres_pod: str = next(
        p.metadata.name for p in kube.list_namespaced_pod("mockexchs").items if "postgres" in p.metadata.name)

    namespace = Namespace("mockexchs")
    namespace.wait_for_pod(postgres_pod)

    namespace.copy("sql/init.sql", f"{postgres_pod}:/tmp/init.sql")
    namespace.exec(postgres_pod, "PGUSER=postgres PGPASSWORD=password psql -a -f /tmp/init.sql")
    logger.info("👌Created sql database.")
    logger.info("👌Deployed bitstamp.\n")
