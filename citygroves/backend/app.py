from pathlib import Path
import os

import pl.devops
from pl.devops import Cluster, Namespace, run


class Backend(pl.devops.App):
    class Links(pl.devops.App.Links):
        cluster: Cluster
        namespace: Namespace

    def __init__(self, li: Links):
        super().__init__("backend", li)

        self.app_root: Path = Path(os.path.realpath(__file__)).parent
