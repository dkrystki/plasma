#!/usr/bin/env python
from pathlib import Path
import os

from loguru import logger

from shangren.utils.deploy import helm_install, run, add_pullsecret
from . import bitstamp


def deploy() -> None:
    os.chdir(Path(__file__).absolute().parent)
    logger.info("🚀Deploying mockexchs")

    namespace: str = "mockexchs"
    add_pullsecret(namespace)
    helm_install(namespace, "postgresql", "stable/postgresql", "6.3.7")
    helm_install(namespace, "redis", "stable/redis", "9.2.0")
    bitstamp.deploy()

    logger.info("👌Deployed mockexchs\n")


if __name__ == "__main__":
    deploy()
