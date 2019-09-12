#!/usr/bin/env python
import os
import sys
from . import bitstamp


def delete() -> None:
    os.chdir(sys.path[0])

    bitstamp.delete()


if __name__ == "__main__":
    delete()
