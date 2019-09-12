#!/usr/bin/env python
from loguru import logger
import graylog
import sentry
import dataprovs


def deploy() -> None:
    logger.info("Deploying services")
    graylog.deploy()
    sentry.deploy()
    dataprovs.deploy()


if __name__ == "__main__":
    deploy()
