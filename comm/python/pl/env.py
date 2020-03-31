import pathlib
import os
from tempfile import NamedTemporaryFile
from typing import Dict, Any, List, Optional


class Path(pathlib.PosixPath):
    def rel(self) -> pathlib.Path:
        """
        Return relavive Path
        :return:
        """
        monorepo_root = pathlib.PosixPath(os.path.realpath(__file__)).parents[3]
        return self.relative_to(monorepo_root)


class Env:
    name: str = "plasma"
    project_code: str = "PL"
    project_name: str = "Plasma"
    project_root: Path = Path()
    project_comm: Path = Path()
    monorepo_root: Path = Path()
    app_root: Path = Path()
    app_src: Path = Path()
    app_name: str = ""
    comm_root: Path = Path()
    emoji: str = ""
    kubeconfig: str
    poetry_ver: str = "1.0.3"
    python_ver_major: int = 3
    python_ver_minor: int = 8
    python_ver_patch: int = 1
    python_ver: str = ""
    skaffold_ver: str = "1.3.1"
    kubectl_ver: str = "1.17.0"
    debian_ver: str = "buster"
    docker_ver: str = "19.03.1"
    helm_ver: str = "2.15.2"
    kind_ver: str = "0.7.0"

    stage: str = ""
    debug: bool = False
    bin_path: Path = Path()
    deps_path: Path = Path()

    class Cluster:
        ip: str = ""
        name: str = ""
        kubernetes_ver: str = ""

    class Registry:
        ip: str = ""
        address: str = ""
        username: str = ""
        password: str = ""

    class AuxCluster:
        ip: str = ""
        address: str = ""

    def __init__(self) -> None:
        self.envs_before: Dict[str, Any] = os.environ.copy()

        if not self.monorepo_root != Path():
            self.monorepo_root = Path(os.path.realpath(__file__)).parents[3]

        if not self.project_root != Path():
            self.project_root = self.monorepo_root

        if not self.app_root != Path():
            self.app_root = self.project_root

        if not self.app_root != Path():
            self.app_src = self.app_root / "flesh"

        if not self.comm_root != Path():
            self.comm_root = self.monorepo_root / "comm"

        self.pyenv_root = self.monorepo_root / ".pyenv"

        if not self.bin_path != Path():
            self.bin_path = self.app_root / Path(".bin")

        if not self.deps_path != Path():
            self.deps_path = self.app_root / Path(".deps")

        if not self.python_ver:
            self.python_ver = f"{self.python_ver_major}.{self.python_ver_minor}.{self.python_ver_patch}"

        self.registry = self.__class__.Registry()
        self.cluster = self.__class__.Cluster()
        self.aux_cluster = self.__class__.AuxCluster()

    def activate(self) -> None:
        self.bin_path.mkdir(exist_ok=True)
        self._set_environ("BIN_PATH", str(self.bin_path))
        self.deps_path.mkdir(exist_ok=True)
        self._set_environ("DEPS_PATH", str(self.deps_path))
        self._set_environ("PROJECT_ROOT", str(self.project_root))
        self._set_environ("APP_ROOT", str(self.app_root))
        self._set_environ("APP_SRC", str(self.app_src))
        self._set_environ("PROJECT_NAME", str(self.project_root))
        self._set_environ("PROJECT_CODE", self.project_code)
        self._set_environ("STAGE", self.stage)
        self._set_environ("STAGE_EMOJI", self.emoji)

        self._set_environ("POETRY_VER", str(self.poetry_ver))
        self._set_environ("PYTHON_VER_MAJOR", str(self.python_ver_major))
        self._set_environ("PYTHON_VER_MINOR", str(self.python_ver_minor))
        self._set_environ("PYTHON_VER_PATCH", str(self.python_ver_patch))
        self._set_environ("PYTHON_VER", f"{self.python_ver_major}.{self.python_ver_minor}.{self.python_ver_patch}")
        self._set_environ("DEBIAN_VER", self.debian_ver)
        self._set_environ("SKAFFOLD_VER", self.skaffold_ver)
        self._set_environ("KUBECTL_VER", self.kubectl_ver)
        self._set_environ("HELM_VER", self.helm_ver)
        self._set_environ("KIND_VER", self.kind_ver)
        self._set_environ("DOCKER_VER", self.docker_ver)

        self._set_environ("CLUSTER_NAME", self.cluster.name)
        self._set_environ("CLUSTER_IP", self.cluster.ip)
        self._set_environ("KUBERNETES_VER", str(self.cluster.kubernetes_ver))

        if self.aux_cluster.ip:
            os.environ["AU_CLUSTER_ADDRESS"] = self.aux_cluster.ip

        self._set_environ("REGISTRY_ADDRESS", self.registry.address)
        self._set_environ("REGISTRY_USERNAME", self.registry.username)
        self._set_environ("REGISTRY_PASSWORD", self.registry.password)
        self._set_environ("REGISTRY_IP", self.registry.ip)

        if "PYTHONPATH" not in os.environ:
            os.environ["PYTHONPATH"] = ""

        os.environ["PL_MONOREPO_ROOT"] = str(self.monorepo_root)
        os.environ["PL_COMM_ROOT"] = str(self.comm_root)
        os.environ["PATH"] = f"{str(self.bin_path)}:{os.environ['PATH']}"
        os.environ["PATH"] = f"{str(self.deps_path)}:{os.environ['PATH']}"
        os.environ["PATH"] = f"{str(self.monorepo_root)}/.venv/bin:{os.environ['PATH']}"
        os.environ["PATH"] = f"{os.environ[f'{self.project_code}_BIN_PATH']}:{os.environ['PATH']}"
        os.environ["KUBECONFIG"] = str(self.project_root / f"envs/{self.stage}/kubeconfig.yaml")
        os.environ["PYTHONPATH"] = f"{str(self.monorepo_root)}/comm/python:{os.environ['PYTHONPATH']}"
        os.environ["PYTHONPATH"] = f"{str(self.monorepo_root.parent)}:{os.environ['PYTHONPATH']}"
        os.environ["PLASMA_DEBUG"] = str(self.debug)
        os.environ["PYENV_ROOT"] = str(self.pyenv_root)
        os.environ["PATH"] = f"{str(self.pyenv_root/'bin')}:{os.environ['PATH']}"

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
            # that's the only way to modify the prompt
            if self.pyenv_root.exists():
                tmprc.write('eval "$(pyenv init -)"\n')
                tmprc.write('pyenv global "$PL_PYTHON_VER" > /dev/null\n')

            tmprc.write(self.as_string(ignore_unchanged=False))
            tmprc.write(f'PS1={self.emoji}\({self.name}\)$PS1\n')

            os.system(f"bash --rcfile {tmprc.name}")

    def _set_environ(self, name: str, value: str) -> None:
        """
        :param name: Without namespace.
        :param value:
        """
        if value:
            os.environ[f"{self.project_code}_{name}"] = value

    def in_project_root(self, func):
        def wrapper(*args, **kwargs):
            os.chdir(str(self.project_root))
            func(*args, **kwargs)
        return wrapper
