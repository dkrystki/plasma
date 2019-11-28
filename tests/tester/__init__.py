from loguru import logger

from shangren.utils.deploy import Namespace


def deploy() -> None:
    logger.info("Deploying apps")
    tests = Namespace("tests")
