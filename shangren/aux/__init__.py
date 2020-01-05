
def deploy() -> None:
    from loguru import logger
    from aux import graylog
    from aux import sentry
    from aux import misc

    logger.info("Deploying auxiliary services.")
    # istio.deploy()
    graylog.deploy()
    sentry.deploy()
    misc.deploy()


if __name__ == "__main__":
    deploy()
