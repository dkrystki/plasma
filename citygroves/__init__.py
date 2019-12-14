
from pathlib import Path
import os

from plasma.utils.deploy import Namespace


def delete() -> None:
    namespace = Namespace("citygroves")

    namespace.helm("postgresql").delete()
    namespace.helm("redis").delete()


def deploy() -> None:
    import manager

    os.chdir(Path(__file__).absolute().parent)

    namespace = Namespace("citygroves")
    namespace.create()
    namespace.helm("postgresql").install(chart="stable/postgresql", version="6.3.7")
    namespace.helm("redis").install(chart="stable/redis", version="9.2.0")

    manager.deploy()


if __name__ == "__main__":
    deploy()
