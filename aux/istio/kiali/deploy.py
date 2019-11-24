#!/usr/bin/env python
import os
from pathlib import Path
from loguru import logger

from shangren.utils.deploy import run


def deploy() -> None:
    os.chdir(Path(__file__).absolute().parent)

    logger.info("🚀Deploying kiali")

    run("kubectl apply -f k8s/secret.yaml")


if __name__ == "__main__":
    deploy()
