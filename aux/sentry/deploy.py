#!/usr/bin/env python
import os
from pathlib import Path
from loguru import logger
from .seed import seed

from shangren.utils.deploy import run


def deploy() -> None:
    os.chdir(Path(__file__).absolute().parent)

    logger.info("🚀Deploying sentry")
    run("helm repo update")
    logger.info("🚀Deploying redis")
    run("""helm upgrade --install --namespace sentry sentry-redis \
           -f values/local/redis.yaml \
           --force --wait=true \
           --timeout=25000 \
           stable/redis --version 9.1.10""")
    logger.info("🚀Deploying postgres")
    run("""helm upgrade --install --namespace sentry sentry-postgresql \
               -f values/local/postgresql.yaml \
               --force --wait=true \
               --timeout=25000 \
               stable/postgresql --version 6.3.6""")
    logger.info("🚀Deploying sentry")
    run("""helm upgrade --install --namespace sentry sentry \
           -f values/local/sentry.yaml \
           --force --wait=true \
           --timeout=25000 \
           stable/sentry --version 2.1.1""")
    seed()
    logger.info("👌Deployed sentry\n")


if __name__ == "__main__":
    deploy()
