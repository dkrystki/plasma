#!/usr/bin/env python3
from loguru import logger

import datacolls
from aux import graylog, sentry


def delete() -> None:
    logger.info("Deleting tester")
    graylog.delete()
    sentry.delete()
    datacolls.delete()


if __name__ == "__main__":
    delete()
