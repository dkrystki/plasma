#!.venv/bin/python
import click

from pathlib import Path
import os
from tempfile import NamedTemporaryFile
from typing import Dict, Any


class Env:
    project_code: str = "CG"
    emoji: str = ""
    kubeconfig: str
    python_ver_major: int = 3
    python_ver_minor: int = 8
    python_ver_patch: int = 1
    skaffold_ver: str = "1.3.1"
    kubectl_ver: str = "1.17.0"
    debian_ver: str = "buster"
    docker_ver: str = "19.03.1"
    cluster_address: str = ""
    registry_address: str = ""
    stage: str

    def __init__(self) -> None:
        self.envs_before: Dict[str, Any] = os.environ.copy()
        self.monorepo_root: Path = Path(os.path.realpath(__file__)).parents[3]
        self.name: str = "plasma"

    def activate(self) -> None:
        os.environ["PL_MONOREPO_ROOT"] = str(self.monorepo_root)
        os.environ["PL_COMM_ROOT"] = str(self.monorepo_root / "comm")

        os.environ["PATH"] = f"{str(self.monorepo_root)}/.bin:{str(self.monorepo_root)}/.venv/bin:{os.environ['PATH']}"
        os.environ["PYTHONPATH"] = f"{str(self.monorepo_root)}/comm/python:{os.environ['PATH']}"

    def print_envs(self) -> None:
        self.activate()
        for key, value in os.environ.items():
            if key in self.envs_before:
                if value == self.envs_before[key]:
                    continue

            if "BASH_FUNC_" not in key:
                print(f'export {key}="{value}";')

        if 'PS1' in os.environ:
            print(f"export PS1={self.emoji}(gn){os.environ['PS1']}")
        print(f'export CUSTOM_PS1="{self.emoji}({self.name})";')

    def shell(self) -> None:
        self.activate()

        with NamedTemporaryFile(mode='w+', buffering=True, delete=False) as tmprc:
            tmprc.write('source ~/.bashrc\n')

            # that's the only way to modify prompt
            tmprc.write(f'PS1={self.emoji}\({self.name}\)$PS1\n')

            # write variables to .bashrc since sourcing may overwrite some of them
            for key, value in os.environ.items():
                if "BASH_FUNC_" not in key:
                    tmprc.write(f'{key}="{value}"\n')

            os.system(f"bash --rcfile {tmprc.name}")


@click.command()
@click.option('--dry-run/--normal-run', default=False)
def command(dry_run):
    en = Env()

    if dry_run:
        en.print_envs()
    else:
        en.shell()


if __name__ == "__main__":
    command()
