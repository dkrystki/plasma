import os
from pathlib import Path
from loguru import logger

from plasma.utils.deploy import run, Namespace

namespace = Namespace("gitlab")
runner = namespace.helm("runner")


def delete() -> None:
    os.chdir(Path(__file__).absolute().parent)

    logger.info("Deleting graylog")
    runner.delete()

    logger.info("Deleting graylog done")


def deploy() -> None:
    os.chdir(Path(__file__).absolute().parent)

    logger.info("🚀Deploying gitlab-runner")
    namespace.create(enable_istio=False, add_pull_secret=True)

    run("helm repo add gitlab https://charts.gitlab.io")

    runner.install(chart="gitlab/gitlab-runner", version="0.12.0")
