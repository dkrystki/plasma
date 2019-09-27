#!/usr/bin/env python
import os
from pathlib import Path
from loguru import logger

from lib.shangren import run


def seed() -> None:
    os.chdir(Path(__file__).absolute().parent)

    logger.info("🌱Seeding graylog")

    mongo_pod: str = run('kubectl -n graylog get pods -l app=mongodb-replicaset -o name | grep -m 1 -o "mongodb.*$"')
    run(f'kubectl -n graylog exec {mongo_pod} -- bash -c "mkdir -p /home/restore"')
    run(f'kubectl -n graylog cp dump {mongo_pod}:home/restore/graylog')
    run(f'kubectl -n graylog exec {mongo_pod} -- bash -c "mongorestore --quiet /home/restore"')

    logger.info("👌Seeding graylog done")


if __name__ == "__main__":
    seed()
