from pathlib import Path
import os

from loguru import logger

from citygroves.core import namespace, stage


def deploy() -> None:
    os.chdir(Path(__file__).absolute().parent)

    logger.info("Deploying appgen.")

    if stage == "stage":
        namespace.helm("manager").install("./chart")
