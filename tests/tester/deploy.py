#!/usr/bin/env python
from loguru import logger
from shangren.utils.deploy import add_pullsecret, run

from shangren.utils.deploy import create_namespace


def deploy() -> None:
    namespace = "tests"
    logger.info("Deploying apps")
    create_namespace(namespace)

    add_pullsecret(namespace)


if __name__ == "__main__":
    deploy()
