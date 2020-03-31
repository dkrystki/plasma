#!/usr/bin/env python3
import os
from pathlib import Path

from shang.utils.deploy import Namespace


def deploy() -> None:
    os.chdir(Path(__file__).absolute().parent)

    datacolls = Namespace("datacolls")
    datacolls.create()
    datacolls.helm_install("influxdb", "stable/influxdb", "1.4.0")


if __name__ == "__main__":
    deploy()
