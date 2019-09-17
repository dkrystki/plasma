#!/usr/bin/env python
import os
from loguru import logger

from shangren.utils.deploy import run
from .helpers import get_pod_name


def seed() -> None:
    os.chdir(os.path.dirname(__file__))

    logger.info("🌱Seeding sentry")

    sentry_pod: str = get_pod_name()
    run(f'kubectl -n sentry cp dump.json {sentry_pod}:home/sentry/dump.json')
    run(f'kubectl -n sentry exec {sentry_pod} -- bash -c "sentry django loaddata /home/sentry/dump.json"')

    logger.info("👌Seeding sentry done")


if __name__ == "__main__":
    seed()
