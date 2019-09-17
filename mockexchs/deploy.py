#!/usr/bin/env python
from pathlib import Path
import os

from loguru import logger

from shangren.utils.deploy import run


def deploy() -> None:
    os.chdir(Path(__file__).absolute().parent)
    logger.info("🚀Deploying mockexchs")
    run("helm repo update")
    logger.info("🚀Deploying postgres")
    run("""helm upgrade --install --namespace=mockexchs mockexchs-postgresql \
           --force --wait=true \
           -f values/local.yaml \
           --timeout=15000 \
           stable/postgresql \
           --version 6.3.7""")
    logger.info("👌Deployed postgres")
    logger.info("👌Deployed mockexchs\n")


if __name__ == "__main__":
    deploy()
