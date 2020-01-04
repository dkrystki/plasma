
def deploy() -> None:
    from pathlib import Path
    import os

    import core
    from loguru import logger

    os.chdir(Path(__file__).absolute().parent)
    logger.info("🚀Deploying frontend.")
