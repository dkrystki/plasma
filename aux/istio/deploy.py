#!/usr/bin/env python
import os
from pathlib import Path
from loguru import logger

from shangren.utils.deploy import run, Namespace


def deploy() -> None:
    os.chdir(Path(__file__).absolute().parent)

    istio_version = "1.3.0"
    run(f"helm repo add istio.io https://storage.googleapis.com/istio-release/releases/{istio_version}/charts/")

    istio = Namespace("istio-system")
    logger.info("🚀Deploying istio")
    istio.helm_install("init", "istio.io/istio-init", istio_version, upgrade=False)
    istio.helm_install("istio", "istio.io/istio", istio_version, upgrade=False)
    logger.info("👌Deployed istio\n")


if __name__ == "__main__":
    deploy()
