from dataclasses import dataclass
from importlib import import_module

from citygroves.frontend.env_comm import FrontendEnvComm
from pl.apps import Skaffold, NodeUtils, DockerUtils

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
        self.env: FrontendEnvComm = import_module(f"plasma.citygroves.frontend.env_{environ.str('CG_STAGE')}").FrontendEnv()
        super().__init__(se, li)

        self.chdir_to_root()

        self.node = NodeUtils(se=NodeUtils.Sets(),
                              li=NodeUtils.Links(env=self.env))

        self.docker = DockerUtils(se=DockerUtils.Sets(),
                                  li=DockerUtils.Links(env=self.env,
                                                       dockerfile=self.dockerfile))
