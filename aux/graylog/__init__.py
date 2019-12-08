import os
from pathlib import Path
from loguru import logger

from shang.utils.deploy import run, Namespace

namespace = Namespace("graylog")


def delete() -> None:
    os.chdir(Path(__file__).absolute().parent)

    logger.info("Deleting graylog")
    run("helm delete --purge graylog-graylog")
    run("helm delete --purge graylog-fluentbit")

    logger.info("Deleting graylog done")


def seed() -> None:
    os.chdir(Path(__file__).absolute().parent)

    logger.info("🌱Seeding graylog")

    mongo_pod: str = namespace.kubectl('get pods -l app=mongodb-replicaset '
                                       '-o name | grep -m 1 -o "graylog-graylog-mongodb.*$"')
    namespace.kubectl(f'exec {mongo_pod} -- bash -c "mkdir -p /home/restore"')
    namespace.kubectl(f'cp dump {mongo_pod}:home/restore/graylog')
    namespace.kubectl(f'exec {mongo_pod} -- bash -c "mongorestore --quiet /home/restore"')

    logger.info("👌Seeding graylog done")


def dump_data() -> None:
    os.chdir(Path(__file__).absolute().parent)

    logger.info("♻️Dumping graylog♻")

    mongo_pod: str = namespace.kubectl('get pods -l app=mongodb-replicaset '
                                       '-o name | grep -m 1 -o "graylog-graylog-mongodb.*$"')
    namespace.kubectl(f'exec {mongo_pod} -- bash -c "mongodump --quiet -d graylog -o /home/dumps"')
    namespace.kubectl(f'cp {mongo_pod}:home/dumps/graylog dump')
    logger.info("♻️Dumping graylog done\n")


def deploy() -> None:
    os.chdir(Path(__file__).absolute().parent)

    logger.info("🚀Deploying graylog")
    namespace.create(enable_istio=False, add_pull_secret=False)

    namespace.helm_install("graylog", "stable/graylog", "1.3.9")
    namespace.kubectl("apply -f k8s/fluentbit-configmap.yaml")
    namespace.helm_install("fluentbit", "stable/fluent-bit", "2.8.2")
    seed()
    logger.info("👌Deployed graylog\n")
