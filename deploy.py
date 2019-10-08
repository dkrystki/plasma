#!/usr/bin/env python
from loguru import logger
import datacolls
import mockexchs
import tests


def deploy() -> None:
    logger.info("Deploying apps")
    datacolls.deploy()
    mockexchs.deploy()
    tests.deploy()


if __name__ == "__main__":
    deploy()
