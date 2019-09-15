#!/usr/bin/env python
import os
from loguru import logger

from shangren.utils.deploy import run

import pexpect


def deploy() -> pexpect.pty_spawn.spawn:
    os.chdir(os.path.dirname(__file__))

    logger.info("Deploying bitstamp")
    skaffold: pexpect.pty_spawn.spawn = pexpect.spawn("")
    skaffold.expect(r".*Watching for changes.*", timeout=60*5)
    return skaffold


if __name__ == "__main__":
    deploy()
