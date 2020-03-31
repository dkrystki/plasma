#!/usr/bin/env python3
from dataclasses import dataclass
from importlib import import_module

import fire
from pl.apps import PythonUtils
from pl.apps.gitlab_runner import GitlabRunner
from pl.apps.graylog import Graylog
from pl.apps.minio import Minio
from pl.apps.registry import Registry
from pl.apps.sentry import Sentry
from pl.cluster import Cluster, Microk8s

from pl.devops import run

import aux.env_comm
import environ

environ = environ.Env()


class Aux(Cluster):
    @dataclass
    class Links(Cluster.Links):
        pass

    def __init__(self, li: Links, env: aux.env_comm.Env) -> None:
        super().__init__(li, env)
        self.env: aux.env_comm.Env = env

        self.python = PythonUtils(se=PythonUtils.Sets(),
                                  li=PythonUtils.Links(env=self.env))

        self.system = self.create_namespace("system")
        self.gitlab = self.create_namespace("gitlab")
        self.graylog = self.create_namespace("graylog")
        self.sentry = self.create_namespace("sentry")

        self.system.create_app("registry", Registry)

        self.gitlab.create_app("minio", Minio)
        self.gitlab.create_app("gitlab-runner", GitlabRunner)
        self.graylog.create_app("graylog", Graylog)
        self.sentry.create_app("sentry", Sentry)

    def add_hosts(self) -> None:
        super().add_hosts()

        cluster_ip = self.li.device.get_ip()

        run(f"""
        sudo hostess add {self.env.registry.address} {cluster_ip}
        sudo hostess add {self.env.graylog.address} {cluster_ip}
        sudo hostess add {self.env.sentry.address} {cluster_ip} 
        """)

    def install_deps(self) -> None:
        self.install_helm()
        self.install_kubectl()
        self.install_hostess()

    def get_ip(self) -> str:
        ip: str = run("hostname -I").split()[0].decode("utf-8")
        return ip


def get_current_cluster() -> Cluster:
    env = import_module(f"aux.env_{environ.str('AU_STAGE')}").Env()

    device = None
    if env.stage in ["local"]:
        device = Microk8s(env)

    aux = Aux(li=Cluster.Links(device=device),
              env=env)
    return aux


if __name__ == "__main__":
    fire.Fire(get_current_cluster())
