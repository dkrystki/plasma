#!/usr/bin/env python
import os
from pathlib import Path
from kubernetes import client

from shangren.utils.deploy import Namespace


def deploy() -> None:
    os.chdir(Path(__file__).absolute().parent)

    datacolls = Namespace("datacolls")
    datacolls.helm_install("influxdb", "stable/influxdb", "1.4.0")


if __name__ == "__main__":
    deploy()
