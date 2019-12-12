from typing import Dict, Any

import yaml
from pathlib import Path

from shang.utils.deploy import run, Namespace, Helm


class Chart:
    def __init__(self, path: str, values: Dict[str, Any]) -> None:
        self.path: Path = Path(path)
        self.name: str = f"{self.path.stem}-e2e"
        self.namespace = Namespace(self.path.parents[0].stem)
        self.values: Dict[str, str] = values

    def start(self) -> None:
        values_file: Path = Path(".values.yaml")
        values_file.write_text(yaml.dump(self.values))

        helm: Helm = self.namespace.helm(self.name)
        if helm.exists():
            helm.delete()
        helm.install(chart=str(self.path), values_path=str(values_file))

        values_file.unlink()

    def delete(self) -> None:
        run(f"helm delete --purge {self.name}")

    def __enter__(self) -> None:
        self.start()

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.delete()
