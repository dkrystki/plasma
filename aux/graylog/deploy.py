#!/usr/bin/env python
import os
from pathlib import Path
from loguru import logger
from .seed import seed

from shangren.utils.deploy import run, helm_install


def deploy() -> None:
    os.chdir(Path(__file__).absolute().parent)

    logger.info("🚀Deploying graylog")
    run("helm repo update")
    namespace = "graylog"

    run("helm repo add elastic https://helm.elastic.co")
    helm_install(namespace, "elasticsearch", "elastic/elasticsearch", "7.4.0")
    run("helm repo add stable https://kubernetes-charts.storage.googleapis.com/")
    helm_install(namespace, "mongodb", "stable/mongodb-replicaset", "3.10.1")
    helm_install(namespace, "graylog", "stable/graylog", "1.3.3")
    helm_install(namespace, "fluentbit", "stable/fluent-bit", "2.7.1")

    seed()
    logger.info("👌Deployed graylog\n")


if __name__ == "__main__":
    deploy()
