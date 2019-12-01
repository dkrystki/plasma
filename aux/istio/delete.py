#!/usr/bin/env python
import os
from pathlib import Path
from loguru import logger

from shang.utils.deploy import run


def delete() -> None:
    os.chdir(Path(__file__).absolute().parent)

    logger.info("Deleting pypi")
    run("helm delete --purge pypi")
    logger.info("Deleting pypi done")


if __name__ == "__main__":
    delete()
