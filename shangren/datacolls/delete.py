#!/usr/bin/env python3
import os
from pathlib import Path
from datacolls import bitstamp


def delete() -> None:
    os.chdir(Path(__file__).absolute().parent)

    bitstamp.delete()


if __name__ == "__main__":
    delete()
