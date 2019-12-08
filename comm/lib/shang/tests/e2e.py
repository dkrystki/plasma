from typing import Dict, Any

import yaml
from pathlib import Path

from shang.utils.deploy import run


class Chart:
    def __init__(self, path: str, values: Dict[str, Any]) -> None:
        self.path: Path = Path(path)
        self.name: str = f"{self.path.stem}-e2e"
        self.namespace: str = self.path.parents[0].stem
        self.values: Dict[str, str] = values

    def start(self) -> None:
        values_file: Path = Path(".values.yaml")
        values_file.write_text(yaml.dump(self.values))

        run(f"helm install {str(self.path)} --name={self.namespace}-{self.name} --namespace={self.namespace}"
            f" --set nameOverride={self.name} -f {str(values_file)} --wait")
        values_file.unlink()

    def delete(self) -> None:
        run(f"helm delete --purge {self.name}")

    def __enter__(self) -> None:
        self.start()

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.delete()