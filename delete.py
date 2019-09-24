#!/usr/bin/env python
from loguru import logger

import datacolls
from aux import graylog, sentry


def delete() -> None:
    logger.info("Deploying services")
    graylog.delete()
    sentry.delete()
    datacolls.delete()


if __name__ == "__main__":
    delete()
