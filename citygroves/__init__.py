
from pathlib import Path
import os


def delete() -> None:
    namespace.helm("postgresql").delete()
    namespace.helm("redis").delete()


def deploy() -> None:
    import core
    import manager
    import frontend
    import appgen

    os.chdir(Path(__file__).absolute().parent)

    core.namespace.create()
    core.namespace.helm("postgresql").install(chart="stable/postgresql", version="6.3.7")
    core.namespace.helm("redis").install(chart="stable/redis", version="9.2.0")

    manager.deploy()
    frontend.deploy()
    appgen.deploy()


if __name__ == "__main__":
    deploy()
