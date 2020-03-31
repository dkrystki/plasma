#!/usr/bin/env python3
from pathlib import Path

import fire
from importlib import import_module
from dataclasses import dataclass

from pl.apps import Skaffold, PythonUtils, Dockerfile

import environ
from pl.env import Env

environ = environ.Env()


class Backend(Skaffold):
    @dataclass
    class Sets(Skaffold.Sets):
        pass

    @dataclass
    class Links(Skaffold.Links):
        pass

    def __init__(self, li: Links, se: Sets):
        super().__init__(se, li)

        self.chdir_to_root()
        self.env: Env = import_module(f"plasma.citygroves.backend.env_{environ.str('CG_STAGE')}").Env()

        self.dockerfile = Dockerfile(
            se=Dockerfile.Sets(template=(self.env.project_comm / "docker/Dockerfile.python.templ"),
                               out_path=Path(f"Dockerfile.{self.env.stage}"),
                               base_image=f"{self.env.registry.address}/{self.env.prebuild_image_name}"),
            li=Dockerfile.Links(env=self.env)
        )

        self.python = PythonUtils(se=PythonUtils.Sets(),
                                  li=PythonUtils.Links(env=self.env))


if __name__ == "__main__":
    from citygroves.cluster import get_current_cluster

    fire.Fire(get_current_cluster().backend)
