from pathlib import Path
import os

from loguru import logger


def deploy() -> None:
    os.chdir(Path(__file__).absolute().parent)

    logger.info("Deploying appgen.")
