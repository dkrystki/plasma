#!/usr/bin/env python
import os
import sys
from loguru import logger
from .seed import seed

from shangren.utils.deploy import run


def deploy() -> None:
    os.chdir(sys.path[0])

    ip: str = run("minikube --profile=shangren ip")

    logger.info("🚀Deploying sentry")
    logger.info("🚀Deploying elasticsearch")
    run("""helm upgrade --install --namespace sentry sentry \\
           -f values/local/sentry.yaml \\
           --force --wait=true \\
           --timeout=25000 \\
           stable/sentry""")
    logger.info("👌Deployed sentry\n")
    seed()


if __name__ == "__main__":
    deploy()
