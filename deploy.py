#!/usr/bin/env python
import subprocess
import sys

from pathlib import Path
from loguru import logger
import dataprovs


def deploy() -> None:
    logger.info("Deploying apps")
    dataprovs.deploy()
    logger.info("🚀starting skaffold")

    Path(__file__).absolute().parent.cwd()
    logger.info(Path(__file__).absolute().parent)
    logger.info(Path(__file__).absolute())
    process = subprocess.Popen("skaffold dev -p local", shell=True, stderr=sys.stdout,
                               stdout=sys.stdout)

    while process.stdout.readable():
        line = process.stdout.readline()

        if not line:
            break

        print(line.strip().decode("utf-8"))


if __name__ == "__main__":
    deploy()
