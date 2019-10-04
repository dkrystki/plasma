#!/usr/bin/env python
import os
from pathlib import Path
from loguru import logger

from shangren.utils.deploy import run


def delete() -> None:
    os.chdir(Path(__file__).absolute().parent)

    logger.info("Deleting sentry")
    run("helm delete --purge redis")
    run("helm delete --purge sentry")
    run("helm delete --purge postgresql")
    logger.info("Deleting sentry done")


if __name__ == "__main__":
    delete()
