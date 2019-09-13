#!/usr/bin/env python
import os
import sys
from loguru import logger
from .seed import seed

from shangren.utils.deploy import run


def deploy() -> None:
    os.chdir(sys.path[0])

    ip: str = run("minikube --profile=shangren ip")

    logger.info("🚀Deploying graylog")
    run("helm repo add elastic https://helm.elastic.co")

    logger.info("🚀Deploying elasticsearch")
    run("""helm upgrade --install --namespace graylog elasticsearch \\
        -f values/local/elasticsearch.yaml \\
        --force --wait=true \\
        --timeout=25000 \\
        elastic/elasticsearch""")

    logger.info("🚀Deploying mongodb")
    run("""helm upgrade --install --namespace graylog mongodb \\
     -f values/local/mongodb.yaml \\
        --force --wait=true \\
        --timeout=25000 \\
        stable/mongodb-replicaset""")

    logger.info("🚀Deploying graylog")
    run("""helm upgrade --install --namespace graylog graylog \
        -f values/local/graylog.yaml \
        --force --wait=true \
        --timeout=25000 \
        stable/graylog""")

    logger.info("🚀Deploying fluentbit")
    run("""helm upgrade --install --namespace graylog \
        -f values/local/fluentbit.yaml --force --wait=true \
         fluentbit stable/fluent-bit""")

    logger.info("👌Deployed graylog\n")
    seed()


if __name__ == "__main__":

    deploy()
