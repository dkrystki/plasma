#!../.venv/bin/python3
from dataclasses import dataclass
from importlib import import_module

import fire
from pl.apps import PythonUtils
from pl.apps.gitlab_runner import GitlabRunner
from pl.apps.minio import Minio
from pl.cluster import Cluster, Microk8s

from pl.devops import run

import aux.env_comm
import environ

environ = environ.Env()


class Aux(Cluster):
    @dataclass
    class Links(Cluster.Links):
        pass

    @dataclass
    class Sets(Cluster.Sets):
        pass

    def __init__(self, li: Links, se: Sets, env: aux.env_comm.AuxEnvComm) -> None:
        super().__init__(li, se, env)
        self.env: aux.env_comm.AuxEnvComm = env

        self.python = PythonUtils(se=PythonUtils.Sets(),
                                  li=PythonUtils.Links(env=self.env))

        self.gitlab = self.create_namespace("gitlab")
        # self.graylog = self.create_namespace("graylog")
        # self.sentry = self.create_namespace("sentry")

        self.gitlab.create_app("minio", Minio)
        self.gitlab.create_app("gitlab-runner", GitlabRunner)
        # self.graylog.create_app("graylog", Graylog)
        # self.sentry.create_app("sentry", Sentry)

    def add_hosts(self) -> None:
        super().add_hosts()

        cluster_ip = self.li.device.get_ip()

        run(f"""
        sudo hostess add {self.env.registry.address} {cluster_ip}
        # sudo hostess add {self.env.graylog.address} {cluster_ip}
        # sudo hostess add {self.env.sentry.address} {cluster_ip} 
        """)

    def install_deps(self) -> None:
        self.install_helm()
        self.install_kubectl()
        self.install_hostess()

    def get_ip(self) -> str:
        ip: str = run("hostname -I").split()[0].decode("utf-8")
        return ip


def get_current_cluster() -> Cluster:
    env = import_module(f"aux.env_{environ.str('AU_STAGE')}").AuxEnv()

    device = None
    if env.stage in ["local"]:
        device = Microk8s(env)

    aux = Aux(li=Cluster.Links(device=device),
              se=Cluster.Sets(deploy_ingress=False),
              env=env)
    return aux


if __name__ == "__main__":
    fire.Fire(get_current_cluster())
