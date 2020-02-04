import os
from typing import List

from plasma.devops import Namespace, App
import plasma.shell
import environ
import shangren.shell
from shangren.aux.gitlab import Gitlab
from shangren.aux.kaniko import Kaniko
from shangren.aux.minio import Minio

environ = environ.Env()


class Cluster(plasma.devops.Cluster):
    def __init__(self, env: shangren.shell.Env):
        super().__init__(env)
        self.env: shangren.shell.Env = env

        self.add_namespace(Namespace(
            li=Namespace.Links(cluster=self),
            name=f"gitlab"),
        )

        self.add_namespace(Namespace(
            li=Namespace.Links(cluster=self),
            name=f"default"),
        )

        self.gitlab = Gitlab(
            li=Gitlab.Links(cluster=self,
                            namespace=self.namespaces["gitlab"]))

        self.minio = Minio(
            li=Gitlab.Links(cluster=self,
                            namespace=self.namespaces["gitlab"]))

        self.kaniko = Kaniko(
            li=Gitlab.Links(cluster=self,
                            namespace=self.namespaces["default"]))

        self.apps: List[App] = [
            self.minio,
            self.gitlab,
            self.kaniko
        ]

    def deploy(self):
        os.chdir(str(self.env.project_root))
        super().deploy()


def get_current_cluster() -> Cluster:
    current_env = shangren.shell.envs[environ.str("SG_STAGE")]
    cluster = Cluster(env=current_env)
    return cluster
