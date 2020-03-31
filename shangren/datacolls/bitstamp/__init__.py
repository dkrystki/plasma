#!/usr/bin/env python3
import os
from pathlib import Path


def deploy():
    os.chdir(Path(__file__).absolute().parent)


if __name__ == "__main__":
    deploy()
