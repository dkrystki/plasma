#!/usr/bin/env python3
from dataclasses import dataclass
from importlib import import_module

import fire
from citygroves.appgen.env_comm import AppgenEnvComm
from pl.apps import Skaffold, DockerUtils, AppPythonUtils

import environ

environ = environ.Env()


class Appgen(Skaffold):
    @dataclass
    class Sets(Skaffold.Sets):
        pass

    @dataclass
    class Links(Skaffold.Links):
        pass

    def __init__(self, li: Links, se: Sets):
        self.env: AppgenEnvComm = import_module(f"plasma.citygroves.appgen.env_{environ.str('CG_STAGE')}").AppgenEnv()
        super().__init__(se, li)

        self.chdir_to_root()

        self.python = AppPythonUtils(se=AppPythonUtils.Sets(),
                                     li=AppPythonUtils.Links(env=self.env))

        self.docker = DockerUtils(se=DockerUtils.Sets(),
                                  li=DockerUtils.Links(env=self.env,
                                                       dockerfile=self.dockerfile))


if __name__ == "__main__":
    from citygroves.cluster import get_current_cluster

    fire.Fire(get_current_cluster().appgen)
