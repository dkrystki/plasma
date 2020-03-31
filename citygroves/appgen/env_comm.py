from pathlib import Path
import os
import plasma.env


class Env(plasma.env.Env):
    helm_release_name = "citygroves-appgen"
    app_name = "appgen"

    def __init__(self) -> None:
        super().__init__()

        self.app_root: Path = Path(os.path.realpath(__file__)).parent
        self.app_src: Path = self.app_root / "flesh"
        self.name: str = "ag"

    def activate(self) -> None:
        super().activate()

        self._set_environ("HELM_RELEASE_NAME", str(self.helm_release_name))
