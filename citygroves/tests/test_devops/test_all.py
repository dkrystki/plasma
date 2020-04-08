from pathlib import Path
from typing import List

import pytest

from pl.devops import run


@pytest.mark.parametrize("stage", ["test", "local"])
def test_shell(env, stage):
    output: List[str] = run(f"./shell.py {stage} --dry-run")
    assert len(output)

    output: List[str] = run(f"./shell.py {stage} --dry-run --save")
    Path(f".env_{stage}").unlink()
    assert len(output) != 0
