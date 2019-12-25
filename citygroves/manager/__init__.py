
def deploy() -> None:
    from pathlib import Path
    import os

    from citygroves.core import namespace, stage
    from loguru import logger

    os.chdir(Path(__file__).absolute().parent)
    logger.info("🚀Deploying manager.")

    logger.info("🚀Creating sql database.")
    postgres_pod: str = next(pod for pod in namespace.get_pods() if "postgres" in pod)

    namespace.wait_for_pod(postgres_pod)

    namespace.copy("sql/init.sql", f"{postgres_pod}:/tmp/init.sql")
    namespace.exec(postgres_pod, "PGUSER=postgres PGPASSWORD=password psql -a -f /tmp/init.sql")
    logger.info("👌Created sql database.")

    if stage == "stage":
        namespace.helm("manager").install("./chart")
