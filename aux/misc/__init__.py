import os
from pathlib import Path
from loguru import logger

from shangren.utils.deploy import run, Namespace


def deploy() -> None:
    os.chdir(Path(__file__).absolute().parent)

    logger.info("🚀Deploying misc apps")

    run("helm repo add owkin https://owkin.github.io/charts")
    run("helm repo update")
    misc = Namespace("misc")
    misc.helm_install("pypi", "owkin/pypiserver", "1.1.0")

    default = Namespace("default")
    default.helm_install("registry", "stable/docker-registry", "1.8.3")

    logger.info("👌Deployed misc apps\n")

