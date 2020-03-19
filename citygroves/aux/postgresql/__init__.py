from pathlib import Path
import os

import pl.apps.postgres


class Postgres(pl.apps.postgres.Postgres):
    class Links(pl.apps.postgres.Postgres.Links):
        pass

    def __init__(self, li: Links):
        super().__init__(li)
        self.app_root: Path = Path(os.path.realpath(__file__)).parent
