#!/usr/bin/env python
import os
import subprocess
import sys

from pathlib import Path
from loguru import logger


def skaffold() -> None:
    logger.info("🚀starting skaffold")

    os.chdir(Path(__file__).absolute().parent)

    process = subprocess.Popen("skaffold dev -p local", shell=True, stderr=sys.stdout,
                               stdout=sys.stdout)
    try:
        process.wait()
    except KeyboardInterrupt:
        process.terminate()
        print("TEST")


if __name__ == "__main__":
    skaffold()
