from pathlib import Path
import os
import plasma.env


class Env(plasma.env.Env):
    helm_release_name = "citygroves-backend"

    def __init__(self) -> None:
        super().__init__()

        self.app_root: Path = Path(os.path.realpath(__file__)).parent
        self.app_src: Path = self.app_root / "flesh"
        self.name: str = "backend"

    def activate(self) -> None:
        super().activate()

        os.environ["PATH"] = f"{str(self.app_root)}/.bin:{os.environ['PATH']}"
        self._set_environ("APP_ROOT", str(self.app_root))
        self._set_environ("APP_SRC", str(self.app_src))
        self._set_environ("HELM_RELEASE_NAME", str(self.helm_release_name))
