#!/usr/bin/env python
import os
import subprocess
import sys

from pathlib import Path
from loguru import logger
import dataprovs
import atexit


def deploy() -> None:
    logger.info("Deploying apps")
    dataprovs.deploy()
    logger.info("🚀starting skaffold")

    os.chdir(Path(__file__).absolute().parent)

    process = subprocess.Popen("skaffold dev -p local", shell=True, stderr=sys.stdout,
                               stdout=sys.stdout)
    try:
        process.wait()
    except KeyboardInterrupt:
        process.terminate()
        print("TEST")

# def on_exit():
#     process.e


if __name__ == "__main__":
    # atexit.register(on_exit)
    deploy()
