#!/usr/bin/env python
from loguru import logger
import graylog
import sentry
import pypi


def deploy() -> None:
    logger.info("Deploying auxiliary services.")
    graylog.deploy()
    sentry.deploy()
    pypi.deploy()


if __name__ == "__main__":
    deploy()
