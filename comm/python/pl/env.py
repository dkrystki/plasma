from pathlib import Path
import os
from tempfile import NamedTemporaryFile
from typing import Dict, Any, List


class Env:
    project_code: str = "CG"
    emoji: str = ""
    kubeconfig: str
    poetry_ver: str = "1.0.3"
    python_ver_major: int = 3
    python_ver_minor: int = 8
    python_ver_patch: int = 1
    skaffold_ver: str = "1.3.1"
    kubectl_ver: str = "1.17.0"
    debian_ver: str = "buster"
    docker_ver: str = "19.03.1"
    cluster_address: str = ""
    registry_address: str = ""
    stage: str = ""
    debug: bool = False

    def __init__(self) -> None:
        self.envs_before: Dict[str, Any] = os.environ.copy()
        self.monorepo_root: Path = Path(os.path.realpath(__file__)).parents[3]
        self.name: str = "plasma"
        self.parent: Any = None

    def activate(self) -> None:
        if self.parent:
            self.parent.activate()

        os.environ["PL_MONOREPO_ROOT"] = str(self.monorepo_root)
        os.environ["PL_COMM_ROOT"] = str(self.monorepo_root / "comm")

        os.environ["PATH"] = f"{str(self.monorepo_root)}/.bin:{os.environ['PATH']}"
        os.environ["PATH"] = f"{str(self.monorepo_root)}/.venv/bin:{os.environ['PATH']}"
        if "PYTHONPATH" not in os.environ:
            os.environ["PYTHONPATH"] = ""
        os.environ["PYTHONPATH"] = f"{str(self.monorepo_root)}/comm/python:{os.environ['PYTHONPATH']}"
        os.environ["PYTHONPATH"] = f"{str(self.monorepo_root.parent)}:{os.environ['PYTHONPATH']}"
        os.environ["PLASMA_DEBUG"] = str(self.debug)
        os.environ["PL_POETRY_VER"] = str(self.poetry_ver)
        os.environ["PL_PYTHON_VER_MAJOR"] = str(self.python_ver_major)
        os.environ["PL_PYTHON_VER_MINOR"] = str(self.python_ver_minor)
        os.environ["PL_PYTHON_VER_PATCH"] = str(self.python_ver_patch)
        os.environ["PL_PYTHON_VER"] = f"{self.python_ver_major}.{self.python_ver_minor}.{self.python_ver_patch}"

    def as_string(self, add_export: bool = True) -> str:
        lines: List[str] = []

        for key, value in os.environ.items():
            if key in self.envs_before:
                if value == self.envs_before[key]:
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
            # that's the only way to modify the prompt
            tmprc.write(self.as_string())
            tmprc.write(f'PS1={self.emoji}\({self.name}\)$PS1\n')

            os.system(f"bash --rcfile {tmprc.name}")
