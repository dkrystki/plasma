#!/usr/bin/env python
import os
from pathlib import Path
from loguru import logger

from shangren.utils.deploy import run


def delete() -> None:
    os.chdir(Path(__file__).absolute().parent)

    logger.info("Deleting bitstamp")
    run("helm delete --purge bitstamp")
    logger.info("Deleting bitstamp done")


if __name__ == "__main__":
    delete()
