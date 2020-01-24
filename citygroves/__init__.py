
from pathlib import Path
import os


def delete() -> None:
    import core
    core.namespace.helm("postgresql").delete()
    core.namespace.helm("redis").delete()


def deploy() -> None:
    import core
    import backend
    import frontend
    import appgen

    os.chdir(Path(__file__).absolute().parent)

    core.namespace.create()
    core.namespace.helm("postgresql").install(chart="stable/postgresql", version="6.3.7")
    core.namespace.helm("redis").install(chart="stable/redis", version="9.2.0")

    backend.deploy()
    frontend.deploy()
    appgen.deploy()


if __name__ == "__main__":
    deploy()
