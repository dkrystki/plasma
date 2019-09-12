#!/usr/bin/env python
import os
import sys
from loguru import logger

from shangren.utils.deploy import run


def delete() -> None:
    os.chdir(sys.path[0])

    logger.info("Deleting bitstamp")
    run("helm delete --purge bitstamp")
    logger.info("Deleting bitstamp done")


if __name__ == "__main__":
    delete()
