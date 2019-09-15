#!/usr/bin/env python
import os
from typing import List

import pexpect
from . import bitstamp


def deploy() -> List[pexpect.pty_spawn.spawn]:
    os.chdir(os.path.dirname(__file__))

    dataprovs: List[pexpect.pty_spawn.spawn] = list()
    dataprovs.append(bitstamp.deploy())
    return dataprovs


if __name__ == "__main__":
    deploy()
