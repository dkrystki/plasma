#!/usr/bin/env python3
import sys

import fire
from pl.devops import run

import environ

environ = environ.Env()

from plasma.env import PlasmaEnv


class Monorepo:
    def __init__(self, env: PlasmaEnv) -> None:
        self.env = env

    def is_ci_job(self) -> bool:
        return "CI_JOB_ID" in environ

    def sudo(self) -> str:
        if self.is_ci_job():
            return ""
        else:
            return "sudo"

    def install_python(self) -> None:
        print(f"Installing Python {self.env.python.ver}")

        run(f"""
        {self.sudo()} apt install curl git-core gcc make zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev libssl-dev
        git clone https://github.com/pyenv/pyenv.git $HOME/.pyenv
        export PYENV_ROOT="$HOME/.pyenv"
        export PATH="$PYENV_ROOT/bin:$PATH"
        eval "$(pyenv init -)"
        pyenv install {self.env.python.ver}
        """)

    def bootstrap(self) -> None:
        print("Bootstrapping Plasma Monorepo")
        if self.is_ci_job():
            run(f"""
                apt update
                apt install sudo -y 
                """)

        if sys.version_info[0] != 3 or sys.version_info[1] != 8 or sys.version_info[2] != 1:
            self.install_python()

    def test(self) -> None:
        print("Testing Plasma common libraries")
        run(f"""
            cd {self.env.root}
            pytest comm/python/tests
            """, print_output=True)


if __name__ == "__main__":
    monorepo = Monorepo(env=PlasmaEnv())
    fire.Fire(monorepo)
