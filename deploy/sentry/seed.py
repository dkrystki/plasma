#!/usr/bin/env python
import os
import sys
from loguru import logger

from shangren.utils.deploy import run
from .helpers import get_pod_name


def seed() -> None:
    os.chdir(sys.path[0])

    logger.info("🌱Seeding sentry")

    sentry_pod: str = get_pod_name()
    run(f'kubectl -n sentry exec {sentry_pod} -- bash -c "sentry django loaddata /home/sentry/dump.json"')

    logger.info("👌Seeding sentry done\n")


if __name__ == "__main__":
    seed()
