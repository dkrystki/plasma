import os
from pathlib import Path

from plasma.env import Env

from plasma.comm.python.pl.devops import run


def test_run():
    run("echo test")


def test_shell():
    env = Env()

    os.chdir(str(env.monorepo_root))
    run("./shell.py")
    run("./shell.py --dry-run")
    run("./shell.py --dry-run --save")

    assert Path(".env").exists()

    Path(".env").unlink()
