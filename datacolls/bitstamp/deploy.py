#!/usr/bin/env python
import os
from pathlib import Path

from shangren.utils.deploy import run


def deploy():
    os.chdir(Path(__file__).absolute().parent)


if __name__ == "__main__":
    deploy()
