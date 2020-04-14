#!/usr/bin/env python3
import fire
from importlib import import_module
from dataclasses import dataclass

from hmlet.env_comm import HmletEnvComm
from hmlet.photos.env_comm import PhotosEnvComm
from pl.apps import Skaffold, DockerUtils, AppPythonUtils

import environ

environ = environ.Env()


class Photos(Skaffold):
    @dataclass
    class Sets(Skaffold.Sets):
        pass

    @dataclass
    class Links(Skaffold.Links):
        pass

    def __init__(self, li: Links, se: Sets):
        self.env: PhotosEnvComm = import_module(
            f"plasma.hmlet.photos.env_{environ.str('HT_STAGE')}"
        ).PhotosEnv()
        super().__init__(se, li)

        self.chdir_to_root()

        self.python = AppPythonUtils(se=AppPythonUtils.Sets(),
                                     li=AppPythonUtils.Links(env=self.env))

        self.docker = DockerUtils(se=DockerUtils.Sets(),
                                  li=DockerUtils.Links(env=self.env,
                                                       dockerfile=self.dockerfile))


if __name__ == "__main__":
    from hmlet.cluster import get_current_cluster

    fire.Fire(get_current_cluster().photos)
