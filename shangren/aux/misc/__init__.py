import os
from pathlib import Path
from loguru import logger

from pl.utils.deploy import run, Namespace


def delete() -> None:
    os.chdir(Path(__file__).absolute().parent)

    Namespace("misc").helm("pypi").delete()
    Namespace("default").helm("registry").delete()


def deploy() -> None:
    os.chdir(Path(__file__).absolute().parent)

    logger.info("🚀Deploying misc apps")

    run("helm repo add owkin https://owkin.github.io/charts")
    run("helm repo update")
    misc = Namespace("misc")
    misc.create()
    misc.helm("pypi").install("owkin/pypiserver", "1.1.0")

    default = Namespace("default")
    default.create()
    default.helm("registry").install("stable/docker-registry", "1.8.3")

    logger.info("👌Deployed misc apps\n")

