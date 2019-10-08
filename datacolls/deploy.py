#!/usr/bin/env python
import os
from pathlib import Path

from shangren.utils.deploy import helm_install, run, add_pullsecret


def deploy() -> None:
    os.chdir(Path(__file__).absolute().parent)

    namespace = "datacolls"
    add_pullsecret(namespace)
    helm_install(namespace, "influxdb", "stable/influxdb", "1.4.0")


if __name__ == "__main__":
    deploy()
