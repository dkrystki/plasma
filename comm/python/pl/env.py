import pathlib
import os
from dataclasses import dataclass, field, fields
from tempfile import NamedTemporaryFile
from typing import Dict, Any, List, Optional


class Path(pathlib.PosixPath):
    def rel(self) -> pathlib.Path:
        """
        Return relavive Path
        :return:
        """
        root = pathlib.PosixPath(os.path.realpath(__file__)).parents[3]
        return self.relative_to(root)


@dataclass
class BaseEnv:
    name: str = ""

    def __init__(self):
        pass

    def _validate(self, parent_name: str):
        for f in fields(self):
            attr: Any = getattr(self, f.name)
            if attr is None:
                # TODO: sometimes prints double dots
                raise RuntimeError(f'Env variable "{parent_name}.{f.name}" is not set!')
            elif issubclass(type(attr), BaseEnv):
                attr._validate(parent_name=f"{parent_name}.{f.name}.")


@dataclass
class Env(BaseEnv):
    @dataclass
    class AuxCluster(BaseEnv):
        ip: str = ""

    @dataclass
    class Python(BaseEnv):
        ver_major: int = None
        ver_minor: int = None
        ver_patch: int = None
        poetry_ver: str = None
        pyenv_root: Path = None

        @property
        def version(self) -> str:
            return f"{self.ver_major}.{self.ver_minor}.{self.ver_patch}"

    root: Path = None
    python: Python = None
    emoji: str = None
    debug: bool = False
    stage: str = None

    def __init__(self) -> None:
        super().__init__()
        self.envs_before: Dict[str, Any] = os.environ.copy()

        self.comm: Path = self.root / "comm"
        self.pyenv_root: Path = self.root / ".pyenv"
        self.bin_path: Path = self.root / Path(".bin")

    def activate(self) -> None:
        self._validate(self.name)

        self.bin_path.mkdir(exist_ok=True)
        self._set_environ("BIN_PATH", str(self.bin_path))

        self._set_environ("POETRY_VER", str(self.python.poetry_ver))
        self._set_environ("PYTHON_VER_MAJOR", str(self.python.ver_major))
        self._set_environ("PYTHON_VER_MINOR", str(self.python.ver_minor))
        self._set_environ("PYTHON_VER_PATCH", str(self.python.ver_patch))
        self._set_environ("PYTHON_VER", self.python.version)

        if "PYTHONPATH" not in os.environ:
            os.environ["PYTHONPATH"] = ""

        os.environ["PYENV_ROOT"] = str(self.pyenv_root)
        os.environ["PL_MONOREPO_ROOT"] = str(self.root)
        os.environ["PL_MONOREPO_COMM_ROOT"] = str(self.comm)
        os.environ["PATH"] = f"{str(self.bin_path)}:{os.environ['PATH']}"
        os.environ["PATH"] = f"{str(self.pyenv_root/'bin')}:{os.environ['PATH']}"
        os.environ["PATH"] = f"{str(self.pyenv_root/'versions')}/{self.python.version}/bin:{os.environ['PATH']}"
        os.environ["PATH"] = f"{str(self.root)}/.venv/bin:{os.environ['PATH']}"
        os.environ["PYTHONPATH"] = f"{str(self.root)}/comm/python:{os.environ['PYTHONPATH']}"
        os.environ["PYTHONPATH"] = f"{str(self.root.parent)}:{os.environ['PYTHONPATH']}"
        os.environ["PLASMA_DEBUG"] = str(self.debug)

    def as_string(self, add_export: bool = True, ignore_unchanged: bool = True) -> str:
        lines: List[str] = []

        for key, value in os.environ.items():
            if ignore_unchanged:
                if key in self.envs_before and value == self.envs_before[key]:
                    continue
            if "BASH_FUNC_" not in key:
                lines.append(f'{"export" if add_export else ""} {key}="{value}";')

        return "\n".join(lines)

    def print_envs(self) -> None:
        self.activate()
        print(self.as_string())

    def dump_dot_env(self) -> None:
        self.activate()
        path = Path(f".env{'_' if self.stage else ''}{self.stage}")
        path.write_text(self.as_string(add_export=False))

    def shell(self) -> None:
        self.activate()

        with NamedTemporaryFile(mode='w+', buffering=True, delete=True) as tmprc:
            tmprc.write('source ~/.bashrc\n')
            tmprc.write(self.as_string(ignore_unchanged=False))
            tmprc.write(f'PS1={self.emoji}\({self.name}\)$PS1\n')

            os.system(f"bash --rcfile {tmprc.name}")

    def _set_environ(self, name: str, value: str) -> None:
        """
        :param name: Without namespace.
        :param value:
        """
        if value:
            os.environ[f"{self.name.upper()}_{name}"] = value

    def chdir_to_monorepo_root(self) -> None:
        os.chdir(str(self.root))

    def _clear_kwargs(self, kwargs: Dict[str, Any]):
        """
        Remove kwargs that aren't in the base class.
        Has to be called before passing kwargs to base dataclass init.
        (We don't want to pass kwargs that are defined in the given base dataclass)

        :param kwargs:
        :return:
        """
        base_fields = [f.name for f in fields(self.__class__.__mro__[2])]
        for k in list(kwargs.keys()):
            if k not in base_fields:
                kwargs.pop(k)

