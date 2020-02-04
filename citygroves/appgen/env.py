#!../../.venv/bin/python
from pathlib import Path
import os

import citygroves.env
import click


class Env(citygroves.env.Env):
    def __init__(self) -> None:
        super().__init__()

        self.app_root: Path = Path(os.path.realpath(__file__)).parent
        self.app_src: Path = self.app_root / "flesh"

        self.name: str = "appgen"

    def activate(self) -> None:
        super().activate()

        os.environ["PATH"] = f"{str(self.app_root)}/bin:{os.environ['PATH']}"
        os.environ["CG_APP_ROOT"] = str(self.app_root)
        os.environ["CG_APP_SRC"] = str(self.app_src)


class Test(Env):
    emoji: str = "🛠️"

    def __init__(self) -> None:
        super().__init__()


class Local(Env):
    emoji: str = "🐣"

    def __init__(self) -> None:
        super().__init__()


class Stage(Env):
    emoji: str = "🤖"

    def __init__(self) -> None:
        super().__init__()


envs = {
    "test": Test(),
    "local": Local(),
    "stage": Stage()
}


@click.command()
@click.argument("stage_name")
@click.option('--dry-run/--normal-run', default=False)
def command(stage_name: str, dry_run):
    stage = envs[stage_name]

    if dry_run:
        stage.print_envs()
    else:
        stage.shell()


if __name__ == "__main__":
    command()
