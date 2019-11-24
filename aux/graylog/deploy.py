#!/usr/bin/env python
import os
from pathlib import Path
from loguru import logger
from .seed import seed

from shangren.utils.deploy import run, Namespace


def deploy() -> None:
    os.chdir(Path(__file__).absolute().parent)

    logger.info("🚀Deploying graylog")
    graylog = Namespace("graylog")

    run("helm repo add elastic https://helm.elastic.co")
    run("helm repo update")

    graylog.helm_install("elasticsearch", "elastic/elasticsearch", "7.4.1")
    run("helm repo add stable https://kubernetes-charts.storage.googleapis.com/")
    run("helm repo update")

    graylog.helm_install("mongodb", "stable/mongodb-replicaset", "3.10.1")
    graylog.helm_install("graylog", "stable/graylog", "1.3.3")
    graylog.helm_install("fluentbit", "stable/fluent-bit", "2.7.1")
    seed()
    logger.info("👌Deployed graylog\n")


if __name__ == "__main__":
    deploy()
