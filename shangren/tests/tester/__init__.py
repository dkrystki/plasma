def deploy() -> None:
    from loguru import logger
    from shang.utils.deploy import Namespace

    logger.info("Deploying apps")
    tests = Namespace("tests")
