import os
import time
from pathlib import Path
from loguru import logger

from shang.utils.deploy import run, Namespace


def deploy() -> None:
    os.chdir(Path(__file__).absolute().parent)

    istio_version = "1.4.0"
    run(f"helm repo add istio.io https://storage.googleapis.com/istio-release/releases/{istio_version}/charts/")

    istio = Namespace("istio-system")
    istio.create()

    logger.info("🚀Deploying istio")
    run("kubectl apply -f k8s/service-account.yaml")

    time.sleep(2)
    istio.helm_install("init", "istio.io/istio-init", istio_version, upgrade=False)
    run("kubectl -n istio-system wait --for=condition=complete job --all")

    time.sleep(2)
    istio.helm_install("istio", "istio.io/istio", istio_version, upgrade=False)
    logger.info("👌Deployed istio\n")
