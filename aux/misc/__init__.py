import os
from pathlib import Path
from loguru import logger

from shang.utils.deploy import run, Namespace


def delete() -> None:
    os.chdir(Path(__file__).absolute().parent)

    Namespace("misc").helm_delete("pypi")
    Namespace("default").helm_delete("registry")


def deploy() -> None:
    os.chdir(Path(__file__).absolute().parent)

    logger.info("🚀Deploying misc apps")

    run("helm repo add owkin https://owkin.github.io/charts")
    run("helm repo update")
    misc = Namespace("misc")
    misc.create()
    misc.helm_install("pypi", "owkin/pypiserver", "1.1.0")

    default = Namespace("default")
    default.create()
    default.helm_install("registry", "stable/docker-registry", "1.8.3")

    logger.info("👌Deployed misc apps\n")

