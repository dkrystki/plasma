#!/usr/bin/env python
import os
from loguru import logger

from shangren.utils.deploy import run


def delete() -> None:
    os.chdir(os.path.dirname(__file__))

    logger.info("Deleting graylog")
    run("helm delete --purge elasticsearch")
    run("helm delete --purge fluentbit")
    run("helm delete --purge mongodb")
    run("helm delete --purge graylog")
    logger.info("Deleting graylog done")


if __name__ == "__main__":
    delete()
