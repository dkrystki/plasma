#!/usr/bin/env python
from pathlib import Path
import os

from kubernetes.stream import stream
from loguru import logger

from shangren.utils.deploy import run, kube
import bitstamp


def deploy() -> None:
    os.chdir(Path(__file__).absolute().parent)
    logger.info("🚀Deploying mockexchs")
    logger.info("🚀Deploying postgres")
    run("helm repo update")
    run("""helm upgrade --install --namespace=mockexchs mockexchs-postgresql \
           --force --wait=true \
           -f values/local.yaml \
           --timeout=15000 \
           stable/postgresql \
           --version 6.3.7""")

    bitstamp.deploy()

    logger.info("👌Deployed postgres")
    logger.info("👌Deployed mockexchs\n")


if __name__ == "__main__":
    deploy()
