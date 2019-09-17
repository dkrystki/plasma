#!/usr/bin/env python
import os
from loguru import logger

from shangren.utils.deploy import run

import pexpect


def deploy():
    os.chdir(os.path.dirname(__file__))


if __name__ == "__main__":
    deploy()
