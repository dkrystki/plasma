import os
from pathlib import Path
from loguru import logger

from pl.utils.deploy import run, Namespace


def delete() -> None:
    os.chdir(Path(__file__).absolute().parent)

    Namespace("default").helm("registry").delete()


def deploy() -> None:
    os.chdir(Path(__file__).absolute().parent)

    logger.info("🚀Deploying misc apps")

    default = Namespace("default")
    default.create()
    default.helm("registry").install("stable/docker-registry", "1.8.3")

    logger.info("👌Deployed misc apps\n")

