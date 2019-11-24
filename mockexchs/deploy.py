#!/usr/bin/env python
from pathlib import Path
import os

from loguru import logger

from shangren.utils.deploy import Namespace
from . import bitstamp


def deploy() -> None:
    os.chdir(Path(__file__).absolute().parent)
    logger.info("🚀Deploying mockexchs")

    namespace = Namespace("mockexchs")
    namespace.helm_install("postgresql", "stable/postgresql", "6.3.7")
    namespace.helm_install("redis", "stable/redis", "9.2.0")

    bitstamp.deploy()

    logger.info("👌Deployed mockexchs\n")


if __name__ == "__main__":
    deploy()
