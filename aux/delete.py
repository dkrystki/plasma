#!/usr/bin/env python
from loguru import logger
from aux import graylog, sentry
from apps import datacolls


def delete() -> None:
    logger.info("Deploying services")
    graylog.delete()
    sentry.delete()
    datacolls.delete()


if __name__ == "__main__":
    delete()
