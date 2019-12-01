import os
from pathlib import Path
from loguru import logger

from shang.utils.deploy import Namespace


def dump_data() -> None:
    os.chdir(Path(__file__).absolute().parent)

    logger.info("♻️Dumping sentry")

    sentry = Namespace("sentry")

    sentry_pod: str = sentry.kubectl('get pods -l role=web -o name | grep -m 1 -o "sentry-web.*$"')

    sentry.kubectl(f'exec {sentry_pod} -- bash -c "sentry export --silent --indent=2 '
                   f'--exclude migrationhistory,permission,savedsearch,contenttype > /home/sentry/dump.json"')
    sentry.kubectl(f'cp {sentry_pod}:home/sentry/dump.json dump.json')
    logger.info("♻️Dumping sentry done\n")


def seed() -> None:
    os.chdir(Path(__file__).absolute().parent)

    logger.info("🌱Seeding sentry")

    sentry = Namespace("sentry")

    sentry_pod: str = sentry.kubectl('get pods -l role=web -o name | grep -m 1 -o "sentry-web.*$"')

    sentry.kubectl(f'cp dump.json {sentry_pod}:home/sentry/dump.json')
    sentry.kubectl(f'exec {sentry_pod} -- bash -c "sentry django loaddata /home/sentry/dump.json"')

    logger.info("👌Seeding sentry done")


def deploy() -> None:
    os.chdir(Path(__file__).absolute().parent)

    logger.info("🚀Deploying sentry")
    sentry = Namespace("sentry")
    sentry.create(enable_istio=False)

    sentry.helm_install("sentry", "stable/sentry", "2.1.1")
    seed()
    logger.info("👌Deployed sentry\n")


def delete() -> None:
    os.chdir(Path(__file__).absolute().parent)

    sentry = Namespace("sentry")

    sentry.helm_delete("sentry")


if __name__ == "__main__":
    deploy()
