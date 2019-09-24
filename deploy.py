#!/usr/bin/env python
from loguru import logger
import datacolls
from .skaffold import skaffold


def deploy() -> None:
    logger.info("Deploying apps")
    datacolls.deploy()
    skaffold()


if __name__ == "__main__":
    deploy()
