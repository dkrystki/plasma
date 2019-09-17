#!/usr/bin/env python
from loguru import logger
import auxiliary


def delete() -> None:
    logger.info("Deploying services")
    # graylog.delete()
    # sentry.delete()
    # dataprovs.delete()


if __name__ == "__main__":
    delete()
