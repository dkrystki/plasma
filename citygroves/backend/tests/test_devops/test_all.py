from pathlib import Path

import pytest
import subprocess

from environ import Env
environ = Env()


@pytest.mark.parametrize("stage", ["test", "local", "stage", "prod"])
def test_envs(stage, copy_shell):
    output: str = subprocess.check_output(f"./shell.py {stage}", shell=True)
    assert output == b""

    output: str = subprocess.check_output(f"./shell.py {stage} --dry-run", shell=True)
    assert output != b""

    output: str = subprocess.check_output(f"./shell.py {stage} --dry-run --save", shell=True)
    Path(f".env_{stage}").unlink()
    assert output != b""
