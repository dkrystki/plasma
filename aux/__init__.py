from loguru import logger
from aux import graylog
from aux import sentry
from aux import misc


def deploy() -> None:
    logger.info("Deploying auxiliary services.")
    graylog.deploy()
    sentry.deploy()
    misc.deploy()


if __name__ == "__main__":
    deploy()
