#!/usr/bin/env python
from loguru import logger
from shangren.utils.deploy import add_pullsecret


def deploy() -> None:
    namespace = "tests"
    logger.info("Deploying apps")

    add_pullsecret(namespace)


if __name__ == "__main__":
    deploy()
