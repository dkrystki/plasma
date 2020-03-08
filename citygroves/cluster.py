import os
from importlib import import_module
from typing import List

from loguru import logger
from pl.devops import Namespace, App
from citygroves.backend.app import Backend
from citygroves import frontend
from citygroves import appgen
import citygroves.shell
from citygroves.aux import keycloak
from shangren.aux import minio
import citygroves.env_comm
import pl.devops
import environ

environ = environ.Env()


class Cluster(pl.devops.Cluster):
    def __init__(self, env: citygroves.env_comm.Env):
        super().__init__(env)
        self.env: citygroves.env_comm.Env = env

        self.namespace = Namespace(
            li=Namespace.Links(cluster=self),
            name=f"citygroves-{env.stage}")

        self.add_namespace(self.namespace)

        self.keycloak = keycloak.Keycloak(
            li=keycloak.Keycloak.Links(cluster=self,
                                       namespace=self.namespace))

        self.minio = minio.Minio(
            li=keycloak.Keycloak.Links(cluster=self,
                                       namespace=self.namespace))

        self.backend = Backend(
            li=Backend.Links(cluster=self,
                                     namespace=self.namespace))
        self.frontend = frontend.Frontend(
            li=frontend.Frontend.Links(cluster=self,
                                       namespace=self.namespace))
        self.appgen = appgen.AppGen(
            li=frontend.Frontend.Links(cluster=self,
                                       namespace=self.namespace)
        )

        self.apps: List[App] = [
            self.minio,
            self.keycloak,
            self.backend,
            self.frontend,
            self.appgen,
        ]

    def deploy(self):
        super().deploy()

        logger.info(f"🚀Deploying postgresql.")
        self.namespace.helm("postgresql").install(chart="stable/postgresql", version="6.3.7")

        logger.info(f"🚀Deploying redis.")
        self.namespace.helm("redis").install(chart="stable/redis", version="9.2.0")


def get_current_cluster() -> Cluster:
    current_env = import_module(f"env_{environ.str('CG_STAGE')}").Env()
    cluster = Cluster(env=current_env)
    return cluster
