#!/usr/bin/env python
import os
from pathlib import Path
from loguru import logger

from shangren.utils.deploy import run, helm_install


def deploy() -> None:
    os.chdir(Path(__file__).absolute().parent)

    logger.info("🚀Deploying datadog")
    run("helm repo add elastic https://helm.elastic.co")
    run("helm repo update")
    helm_install("datadog", "datadog", "stable/datadog", "1.37.0")

    logger.info("👌Deployed datadog\n")


if __name__ == "__main__":
    deploy()
