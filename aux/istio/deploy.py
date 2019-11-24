#!/usr/bin/env python
import os
from pathlib import Path
from loguru import logger

from shangren.utils.deploy import run, helm_install, kube


def deploy() -> None:
    os.chdir(Path(__file__).absolute().parent)

    logger.info("🚀Deploying istio")
    run("istioctl manifest generate -f values/local/istio.yaml > manifest.yaml")
    run("kubectl apply -f manifest.yaml")
    # run("rm manifest.yaml")
    logger.info("👌Deployed istio\n")


if __name__ == "__main__":
    deploy()
