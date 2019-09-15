#!/usr/bin/env python
from typing import List

import pexpect
from loguru import logger
from apps import dataprovs


def deploy() -> None:
    logger.info("Deploying apps")
    apps: List[pexpect.pty_spawn.spawn] = dataprovs.deploy()
    a = 1


if __name__ == "__main__":
    deploy()
