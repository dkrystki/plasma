#!/usr/bin/env python
import os
from pathlib import Path
from loguru import logger
from .seed import seed

from shangren.utils.deploy import run, helm_install


def deploy() -> None:
    os.chdir(Path(__file__).absolute().parent)

    logger.info("🚀Deploying sentry")
    run("helm repo update")
    namespace = "sentry"

    helm_install(namespace, "redis", "stable/redis", "9.1.10")
    helm_install(namespace, "postgresql", "stable/postgresql", "6.3.6")
    helm_install(namespace, "sentry", "stable/sentry", "2.1.1")
    seed()
    logger.info("👌Deployed sentry\n")


if __name__ == "__main__":
    deploy()
