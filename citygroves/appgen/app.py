from dataclasses import dataclass
from importlib import import_module

import fire
from pl.apps import Skaffold, PythonUtils

import environ

environ = environ.Env()


class AppGen(Skaffold):
    @dataclass
    class Sets(Skaffold.Sets):
        pass

    @dataclass
    class Links(Skaffold.Links):
        pass

    def __init__(self, li: Links, se: Sets):
        super().__init__(se, li)

        self.chdir_to_root()
        self.env = import_module(f"plasma.citygroves.appgen.env_{environ.str('CG_STAGE')}").Env()

        self.python = PythonUtils(se=PythonUtils.Sets(),
                                  li=PythonUtils.Links(env=self.env))


if __name__ == "__main__":
    from citygroves.cluster import get_current_cluster

    fire.Fire(get_current_cluster().appgen)
