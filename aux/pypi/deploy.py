#!/usr/bin/env python
import os
from pathlib import Path
from loguru import logger

from lib.shangren import run


def deploy() -> None:
    os.chdir(Path(__file__).absolute().parent)

    logger.info("🚀Deploying pypi")
    run("helm repo add owkin https://owkin.github.io/charts")
    run("""helm upgrade --install --namespace misc pypi \
           -f values/local/pypi.yaml \
           --force --wait=true \
           --timeout=25000 \
           owkin/pypiserver --version 1.1.0""")
    logger.info("👌Deployed pypi\n")


if __name__ == "__main__":
    deploy()
