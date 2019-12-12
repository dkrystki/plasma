
def deploy() -> None:
    from loguru import logger

    logger.info("Deploying apps")
    datacolls.deploy()
    mockexchs.deploy()
    tests.deploy()


if __name__ == "__main__":
    deploy()
