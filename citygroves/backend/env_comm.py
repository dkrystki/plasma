from plasma.env import Path
import os
import plasma.env


class Env(plasma.env.Env):
    helm_release_name = "citygroves-backend"
    app_name = "backend"
    prebuild: bool = False

    def __init__(self) -> None:
        super().__init__()

        self.app_root: Path = Path(os.path.realpath(__file__)).parent
        self.prebuild_image_name = f"{self.stage}/flesh/{self.app_name}-prebuild"
        self.app_src: Path = self.app_root / "flesh"
        self.name: str = "be"

    def activate(self) -> None:
        super().activate()

        self._set_environ("HELM_RELEASE_NAME", str(self.helm_release_name))
