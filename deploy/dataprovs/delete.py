#!/usr/bin/env python
import os
from . import bitstamp


def delete() -> None:
    os.chdir(os.path.dirname(__file__))

    bitstamp.delete()


if __name__ == "__main__":
    delete()
