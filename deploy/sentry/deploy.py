#!/usr/bin/env python
import os
from loguru import logger
from seed import seed

from shangren.utils.deploy import run


def deploy() -> None:
    os.chdir(os.path.dirname(__file__))

    ip: str = run("minikube --profile=shangren ip")

    logger.info("🚀Deploying sentry")
    run("helm repo update")
    run("""helm upgrade --install --namespace sentry redis \\
           -f values/local/redis.yaml \\
           --force --wait=true \\
           --timeout=25000 \\
           stable/redis --version 9.1.10""")
    run("""helm upgrade --install --namespace sentry postgresql \\
               -f values/local/postgresql.yaml \\
               --force --wait=true \\
               --timeout=25000 \\
               stable/postgresql --version 6.3.6""")
    run("""helm upgrade --install --namespace sentry sentry \
           -f values/local/sentry.yaml \
           --force --wait=true \
           --timeout=25000 \
           stable/sentry --version 2.1.1""")
    seed()
    logger.info("👌Deployed sentry\n")


if __name__ == "__main__":
    deploy()
