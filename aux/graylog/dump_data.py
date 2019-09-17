#!/usr/bin/env python
import os
from pathlib import Path
from loguru import logger

from shangren.utils.deploy import run


def dump_data() -> None:
    os.chdir(Path(__file__).absolute().parent)

    logger.info("♻️Dumping graylog♻")

    mongo_pod: str = run('kubectl -n graylog get pods -l app=mongodb-replicaset -o name | grep -m 1 -o "mongodb.*$"')
    run(f'kubectl -n graylog exec {mongo_pod} -- bash -c "mongodump --quiet -d graylog -o /home/dumps')
    run(f'kubectl -n graylog cp {mongo_pod}:home/dumps/graylog dump')
    logger.info("♻️Dumping graylog done\n")


if __name__ == "__main__":
    dump_data()
