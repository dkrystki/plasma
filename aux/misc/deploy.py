#!/usr/bin/env python
import os
from pathlib import Path
from loguru import logger

from shangren.utils.deploy import run, helm_install, kube


def deploy() -> None:
    os.chdir(Path(__file__).absolute().parent)

    logger.info("🚀Deploying pypi")

    run("helm repo add owkin https://owkin.github.io/charts")
    helm_install("misc", "pypi", "owkin/pypiserver", "1.1.0")
    helm_install("default", "registry", "stable/docker-registry", "1.8.3")
    helm_install("", "registry", "stable/docker-registry", "1.8.3")

    logger.info("👌Deployed pypi\n")


if __name__ == "__main__":
    deploy()
