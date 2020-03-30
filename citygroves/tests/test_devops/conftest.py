import shutil
from pathlib import Path

from pytest import fixture

from environ import Env
environ = Env()


@fixture
def copy_shell():
    shutil.copy(Path(environ.str("CG_PROJECT_ROOT")) / "shell.py", "./shell.py")
    yield
    Path("./shell.py").unlink()
