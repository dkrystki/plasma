#!/usr/bin/env python
from loguru import logger
import datacolls
import mockexchs
from skaffold import skaffold


def deploy() -> None:
    logger.info("Deploying apps")
    datacolls.deploy()
    mockexchs.deploy()
    skaffold()


if __name__ == "__main__":
    deploy()
