#!/usr/bin/env python
import os
from pathlib import Path
from loguru import logger

from shangren.utils.deploy import run, helm_install, kube


def deploy() -> None:
    os.chdir(Path(__file__).absolute().parent)

    logger.info("🚀Deploying istio")

    run("helm repo add istio.io https://storage.googleapis.com/istio-release/releases/1.4.0/charts/")
    helm_install("istio-system", "istio-init", "istio.io/istio-init", "1.4.0", upgrade=False)
    helm_install("istio-system", "istio", "istio.io/istio", "1.4.0", upgrade=False)
    logger.info("👌Deployed istio\n")


if __name__ == "__main__":
    deploy()
