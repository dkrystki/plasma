#!/usr/bin/env python
from pathlib import Path

from loguru import logger

from shangren.utils.deploy import run


def deploy() -> None:
    Path(__file__).absolute().parent.cwd()
    logger.info("🚀Deploying influxdb")
    run("""helm upgrade --install --namespace=$DATAPROVS_NAMESPACE influxdb \
           --force --wait=true \
           --timeout=15000 \
           stable/influxdb \
           --version 1.4.0""")
    logger.info("🚀Starting skaffold")
    logger.info("👌Deployed influxdb\n")


if __name__ == "__main__":
    deploy()
