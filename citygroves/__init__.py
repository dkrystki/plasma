
from pathlib import Path
import os

from citygroves.core import namespace


def delete() -> None:
    namespace.helm("postgresql").delete()
    namespace.helm("redis").delete()


def deploy() -> None:
    import manager

    os.chdir(Path(__file__).absolute().parent)

    namespace.create()
    namespace.helm("postgresql").install(chart="stable/postgresql", version="6.3.7")
    namespace.helm("redis").install(chart="stable/redis", version="9.2.0")

    manager.deploy()


if __name__ == "__main__":
    deploy()
