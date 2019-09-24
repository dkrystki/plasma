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
           -f values/local/postgres.yaml \
           --timeout=15000 \
           stable/postgresql \
           --version 6.3.7""")

    logger.info("🚀Deploying redis")
    run("""helm upgrade --install --namespace=mockexchs mockexchs-redis \
           --force --wait=true \
           -f values/local/redis.yaml \
           --timeout=15000 \
           stable/redis \
           --version 9.2.0""")

    bitstamp.deploy()

    logger.info("👌Deployed postgres")
    logger.info("👌Deployed mockexchs\n")


if __name__ == "__main__":
    deploy()
