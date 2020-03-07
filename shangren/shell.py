#!../.venv/bin/python
from typing import Dict

import click

from shangren.env_comm import Env


envs: Dict[str, Env] = {}

try:
    from shangren.env_test import Test
    envs["test"] = Test()
except ImportError:
    pass

try:
    from shangren.env_local import Local
    envs["local"] = Local()
except ImportError:
    pass

try:
    from shangren.env_stage import Stage
    envs["stage"] = Stage()
except ImportError:
    pass


@click.command()
@click.argument("stage_name", default="local")
@click.option('--dry-run/--normal-run', default=False)
def command(stage_name: str, dry_run):
    env = envs[stage_name]

    if dry_run:
        env.print_envs()
    else:
        env.shell()


if __name__ == "__main__":
    command()
