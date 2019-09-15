#!/usr/bin/env python
from loguru import logger
from aux import graylog, sentry


def deploy() -> None:
    logger.info("Deploying auxiliary services.")
    graylog.deploy()
    sentry.deploy()


if __name__ == "__main__":
    deploy()
