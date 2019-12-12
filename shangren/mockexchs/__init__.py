from pathlib import Path
import os

from loguru import logger

from shang.utils.deploy import Namespace
from mockexchs import bitstamp

namespace = Namespace("mockexchs")


def delete() -> None:
    namespace.helm_delete("postgresql")
    namespace.helm_delete("redis")


def deploy() -> None:
    os.chdir(Path(__file__).absolute().parent)
    logger.info("🚀Deploying mockexchs")

    namespace.create()
    namespace.helm_install("postgresql", "stable/postgresql", "6.3.7")
    namespace.helm_install("redis", "stable/redis", "9.2.0")

    bitstamp.deploy()

    logger.info("👌Deployed mockexchs\n")
