from importlib import import_module

from pl.apps.cert_manager import CertManager
from pl.apps.ingress import Ingress
from pl.apps.kaniko import Kaniko
from pl.apps.keycloak import Keycloak
from pl.apps.postgres import Postgres
from pl.apps.redis import Redis
from pl.apps.registry import Registry
from pl.devops import Namespace, SkaffoldApp

import citygroves.shell
import citygroves.env_comm
import pl.devops
import environ

environ = environ.Env()


class Cluster(pl.devops.Cluster):
    def __init__(self, env: citygroves.env_comm.Env):

        super().__init__(env)
        self.env: citygroves.env_comm.Env = env

        self.aux = self.create_namespace("aux")
        self.system = self.create_namespace("system")
        # self.cert_manager = self.create_namespace("cert-manager")
        # self.flesh = self.create_namespace("flesh")

        # self.cert_manager.create_app("cert-manager", CertManager)
        self.system.create_app("ingress", Ingress)
        self.system.create_app("registry", Registry)

        self.aux.create_app("postgresql", Postgres)
        self.aux.create_app("keycloak", Keycloak)
        self.aux.create_app("redis", Redis)

        self.flesh.create_app("backend", SkaffoldApp)
        self.flesh.create_app("appgen", SkaffoldApp)
        self.flesh.create_app("frontend", SkaffoldApp)

    def deploy(self):
        super().deploy()

        # self.cert_manager.deploy()
        self.system.deploy()
        self.aux.deploy()
        self.flesh.deploy()


def get_current_cluster() -> Cluster:
    current_env = import_module(f"env_{environ.str('CG_STAGE')}").ClusterEnv()
    cluster = Cluster(env=current_env)
    return cluster


# import os
# from typing import List
#
# from pl.devops import Namespace, App
# import pl.env
# import environ
# import shangren.shell
# from shangren.aux.gitlab import Gitlab
# from shangren.aux.kaniko import Kaniko
# from shangren.aux.minio import Minio
#
# environ = environ.Env()
#
#
# class Cluster(pl.devops.Cluster):
#     def __init__(self, env: shangren.shell.Env):
#         super().__init__(env)
#         self.env: shangren.shell.Env = env
#
#         self.add_namespace(Namespace(
#             li=Namespace.Links(cluster=self),
#             name=f"gitlab"),
#         )
#
#         self.add_namespace(Namespace(
#             li=Namespace.Links(cluster=self),
#             name=f"default"),
#         )
#
#         self.gitlab = Gitlab(
#             li=Gitlab.Links(cluster=self,
#                             namespace=self.namespaces["gitlab"]))
#
#         self.minio = Minio(
#             li=Gitlab.Links(cluster=self,
#                             namespace=self.namespaces["gitlab"]))
#
#         self.kaniko = Kaniko(
#             li=Gitlab.Links(cluster=self,
#                             namespace=self.namespaces["default"]))
#
#         self.apps: List[App] = [
#             self.minio,
#             self.gitlab,
#             self.kaniko
#         ]
#
#     def deploy(self):
#         os.chdir(str(self.env.project_root))
#         super().deploy()
#
#
# def get_current_cluster() -> Cluster:
#     current_env = shangren.shell.envs[environ.str("SG_STAGE")]
#     cluster = Cluster(env=current_env)
#     return cluster
