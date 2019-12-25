
def deploy() -> None:
    from pathlib import Path
    import os

    from citygroves.core import namespace, stage
    from loguru import logger

    os.chdir(Path(__file__).absolute().parent)
    logger.info("🚀Deploying frontend.")

    if stage == "stage":
        namespace.helm("frontend").install("./chart")
