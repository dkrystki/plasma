#!/usr/bin/env python
import os
import sys
from loguru import logger

from shangren.utils.deploy import run

import pexpect


def deploy() -> pexpect.pty_spawn.spawn:
    os.chdir(sys.path[0])

    logger.info("Deploying bitstamp")
    skaffold: pexpect.pty_spawn.spawn = pexpect.spawn("skaffold dev -p local")
    skaffold.expect(r".*Watching for changes.*",)
    return skaffold


if __name__ == "__main__":
    deploy()
