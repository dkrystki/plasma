import os
from pathlib import Path
from loguru import logger

from shangren.utils.deploy import run, Namespace

namespace = Namespace("graylog", enable_istio=False, add_pull_secret=False)


def seed() -> None:
    os.chdir(Path(__file__).absolute().parent)

    logger.info("🌱Seeding graylog")

    mongo_pod: str = namespace.kubectl('get pods -l app=mongodb-replicaset -o name | grep -m 1 -o "mongodb.*$"')
    namespace.kubectl(f'exec {mongo_pod} -- bash -c "mkdir -p /home/restore"')
    namespace.kubectl(f'cp dump {mongo_pod}:home/restore/graylog')
    namespace.kubectl(f'exec {mongo_pod} -- bash -c "mongorestore --quiet /home/restore"')

    logger.info("👌Seeding graylog done")


def dump_data() -> None:
    os.chdir(Path(__file__).absolute().parent)

    logger.info("♻️Dumping graylog♻")

    mongo_pod: str = namespace.kubectl('get pods -l app=mongodb-replicaset -o name | grep -m 1 -o "mongodb.*$"')
    namespace.kubectl(f'exec {mongo_pod} -- bash -c "mongodump --quiet -d graylog -o /home/dumps"')
    namespace.kubectl(f'cp {mongo_pod}:home/dumps/graylog dump')
    logger.info("♻️Dumping graylog done\n")


def deploy() -> None:
    os.chdir(Path(__file__).absolute().parent)

    logger.info("🚀Deploying graylog")

    run("helm repo add elastic https://helm.elastic.co")
    run("helm repo update")

    namespace.helm_install("elasticsearch", "elastic/elasticsearch", "7.4.1")
    run("helm repo add stable https://kubernetes-charts.storage.googleapis.com/")
    run("helm repo update")

    namespace.helm_install("mongodb", "stable/mongodb-replicaset", "3.10.1")
    namespace.helm_install("graylog", "stable/graylog", "1.3.3")
    namespace.kubectl("apply -f k8s/fluentbit-configmap.yaml")
    namespace.helm_install("fluentbit", "stable/fluent-bit", "2.8.2")
    seed()
    logger.info("👌Deployed graylog\n")
