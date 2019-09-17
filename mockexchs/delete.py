#!/usr/bin/env python
import os
from pathlib import Path
from dataprovs import bitstamp


def delete() -> None:
    os.chdir(Path(__file__).absolute().parent)

    bitstamp.delete()


if __name__ == "__main__":
    delete()
