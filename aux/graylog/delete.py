#!/usr/bin/env python
import os
from pathlib import Path
from loguru import logger

from shangren.utils.deploy import run


# TODO: FIx that


def delete() -> None:
    os.chdir(Path(__file__).absolute().parent)

    logger.info("Deleting graylog")
    run("helm delete --purge elasticsearch")
    run("helm delete --purge fluentbit")
    run("helm delete --purge mongodb")
    run("helm delete --purge graylog")
    logger.info("Deleting graylog done")


if __name__ == "__main__":
    delete()
