from importlib import import_module

from pl.apps.gitlab_runner import GitlabRunner
from pl.apps.graylog import Graylog
from pl.apps.ingress import Ingress
from pl.apps.minio import Minio
from pl.apps.registry import Registry
from pl.apps.sentry import Sentry
from pl.devops import Namespace

import citygroves.shell
import citygroves.env_comm
import pl.devops
import environ

environ = environ.Env()


class Cluster(pl.devops.Cluster):
    def __init__(self, env: citygroves.env_comm.Env):
        super().__init__(env)
        self.env: citygroves.env_comm.Env = env

        self.system = self.create_namespace("system")
        self.gitlab = self.create_namespace("gitlab")
        self.graylog = self.create_namespace("graylog")
        self.sentry = self.create_namespace("sentry")

        # self.system.create_app("ingress", Ingress)
        self.system.create_app("registry", Registry)

        self.gitlab.create_app("minio", Minio)
        self.gitlab.create_app("gitlab-runner", GitlabRunner)
        self.graylog.create_app("graylog", Graylog)
        self.sentry.create_app("sentry", Sentry)

    def deploy(self):
        super().deploy()

        self.system.deploy()
        self.gitlab.deploy()
        # self.graylog.deploy()
        # self.sentry.deploy()


def get_current_cluster() -> Cluster:
    current_env = import_module(f"env_{environ.str('AU_STAGE')}").Env()
    cluster = Cluster(env=current_env)
    return cluster

