
def deploy() -> None:
    from pathlib import Path
    import os

    from citygroves import core
    from loguru import logger

    os.chdir(Path(__file__).absolute().parent)
    logger.info("🚀Deploying backend.")

    logger.info("🚀Creating sql database.")
    postgres_pod: str = next(pod for pod in core.namespace.get_pods() if "postgres" in pod)

    core.namespace.wait_for_pod(postgres_pod)

    core.namespace.copy("sql/init.sql", f"{postgres_pod}:/tmp/init.sql")
    core.namespace.exec(postgres_pod, "PGUSER=postgres PGPASSWORD=password psql -a -f /tmp/init.sql")
    logger.info("👌Created sql database.")


def delete() -> None:
    from loguru import logger

    logger.info("Delete backend.")
