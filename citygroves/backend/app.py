#!/usr/bin/env python3
import fire
from importlib import import_module
from dataclasses import dataclass

from pl.apps import Skaffold, PythonUtils, DockerUtils, AppPythonUtils

import environ
from plasma.citygroves.backend.env_comm import BackendEnvComm

environ = environ.Env()


class Backend(Skaffold):
    @dataclass
    class Sets(Skaffold.Sets):
        pass

    @dataclass
    class Links(Skaffold.Links):
        pass

    def __init__(self, li: Links, se: Sets):
        self.env: BackendEnvComm = import_module(
            f"plasma.citygroves.backend.env_{environ.str('CG_STAGE')}"
        ).BackendEnv()
        super().__init__(se, li)

        self.chdir_to_root()

        self.python = AppPythonUtils(se=PythonUtils.Sets(),
                                     li=PythonUtils.Links(env=self.env))

        self.docker = DockerUtils(se=DockerUtils.Sets(),
                                  li=DockerUtils.Links(env=self.env,
                                                       dockerfile=self.dockerfile))


if __name__ == "__main__":
    from citygroves.cluster import get_current_cluster

    fire.Fire(get_current_cluster().backend)
