#!/usr/bin/env python
from loguru import logger
import dataprovs
from .skaffold import skaffold


def deploy() -> None:
    logger.info("Deploying apps")
    dataprovs.deploy()
    skaffold()


if __name__ == "__main__":
    deploy()
