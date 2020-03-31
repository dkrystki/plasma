from dataclasses import dataclass
from importlib import import_module

from pl.apps import Skaffold

import environ

environ = environ.Env()


class Frontend(Skaffold):
    @dataclass
    class Sets(Skaffold.Sets):
        pass

    @dataclass
    class Links(Skaffold.Links):
        pass

    def __init__(self, li: Links, se: Sets):
        super().__init__(se, li)

        self.chdir_to_root()
        self.env = import_module(f"plasma.citygroves.frontend.env_{environ.str('CG_STAGE')}").Env()
