#!/usr/bin/env python
from pathlib import Path
from loguru import logger

from shangren.utils.deploy import run
from helpers import get_pod_name


def dump_data() -> None:
    Path(__file__).absolute().parent.cwd()

    logger.info("♻️Dumping sentry")
    sentry_pod: str = get_pod_name()

    run(f'kubectl -n sentry exec {sentry_pod} -- bash -c "sentry export --silent --indent=2 '
        f'--exclude migrationhistory,permission,savedsearch,contenttype > /home/sentry/dump.json"')
    run(f'kubectl -n sentry cp {sentry_pod}:home/sentry/dump.json dump.json')
    logger.info("♻️Dumping sentry done\n")


if __name__ == "__main__":
    dump_data()
