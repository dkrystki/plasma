#!/usr/bin/env python
import os
from pathlib import Path
from loguru import logger
from .seed import seed

from shangren.utils.deploy import Namespace


def deploy() -> None:
    os.chdir(Path(__file__).absolute().parent)

    logger.info("🚀Deploying sentry")
    sentry = Namespace("sentry")

    sentry.helm_install("redis", "stable/redis", "9.1.10")
    sentry.helm_install("postgresql", "stable/postgresql", "6.3.6")
    sentry.helm_install("sentry", "stable/sentry", "2.1.1")
    seed()
    logger.info("👌Deployed sentry\n")


if __name__ == "__main__":
    deploy()
