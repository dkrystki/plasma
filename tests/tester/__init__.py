from loguru import logger

from shang.utils.deploy import Namespace


def deploy() -> None:
    logger.info("Deploying apps")
    tests = Namespace("tests")
