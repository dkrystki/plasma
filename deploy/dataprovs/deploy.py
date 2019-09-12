#!/usr/bin/env python
import os
import sys
from loguru import logger
from . import bitstamp


def deploy() -> None:
    bitstamp.deploy()


if __name__ == "__main__":
    deploy()
