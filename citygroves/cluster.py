#!/usr/bin/env python3
import fire

from dataclasses import dataclass
from importlib import import_module

from citygroves.appgen.app import AppGen
from citygroves.backend.app import Backend
from citygroves.frontend.app import Frontend
from pl.apps import PythonUtils
from pl.apps.ingress import Ingress
from pl.apps.keycloak import Keycloak
from pl.apps.postgres import Postgres
from pl.apps.redis import Redis
from pl.apps.registry import Registry
from pl import cluster
from pl.devops import run

import citygroves.shell
import citygroves.env_comm
import environ

environ = environ.Env()


class Citygroves(cluster.Cluster):
    @dataclass
    class Links(cluster.Cluster.Links):
        pass

    def __init__(self, li: Links, env: citygroves.env_comm.Env):
        super().__init__(li, env)

        self.env: citygroves.env_comm.Env = env

        self.python = PythonUtils(se=PythonUtils.Sets(),
                                  li=PythonUtils.Links(env=self.env))

        self.system = self.create_namespace("system")
        self.aux = self.create_namespace("aux")
        self.flesh = self.create_namespace("flesh")

        self.system.create_app("ingress", Ingress)
        self.system.create_app("registry", Registry)

        postgres = self.aux.create_app("postgresql", Postgres)
        self.aux.create_app("keycloak", Keycloak, extra_links={"postgres": postgres})
        self.aux.create_app("redis", Redis)

        self.backend: Backend = self.flesh.create_app("backend", Backend)
        self.appgen: AppGen = self.flesh.create_app("appgen", AppGen)
        self.frontend: Frontend = self.flesh.create_app("frontend", Frontend)

    def install_deps(self) -> None:
        super().install_deps()
        self.install_hostess()
        self.install_kubectl()
        self.install_helm()
        self.install_skaffold()
        self.install_kind()

    def bootstrap_local_dev(self) -> None:
        self.install_deps()

        self.backend.python.bootstrap_local_dev()
        self.appgen.python.bootstrap_local_dev()

    def add_hosts(self):
        super().add_hosts()

        cluster_ip = self.li.device.get_ip()

        run(f"""
            {self.sudo()} hostess add {self.env.registry.address} {self.env.registry.ip}
            {self.sudo()} hostess add {self.env.keycloak.address} {cluster_ip}
            {self.sudo()} hostess add {self.env.backend.address} {cluster_ip}
            {self.sudo()} hostess add {self.env.appgen.address} {cluster_ip}
            {self.sudo()} hostess add {self.env.frontend.address} {cluster_ip}
            """)

    def build_ci_images(self):
        run(f"""
            docker login aux.registry.local --username {self.env.registry.username} -p{self.env.registry.password}

            docker build -f {self.env.project_comm}/docker/Dockerfile.python-ci \\
              -t python-cg-ci {self.env.monorepo_root} \\
              --build-arg PYTHON_VER_MAJOR={self.env.python_ver_major} \\
              --build-arg PYTHON_VER_MINOR={self.env.python_ver_minor} \\
              --build-arg PYTHON_VER_PATCH={self.env.python_ver_patch} \\
              --build-arg DEBIAN_VER={self.env.debian_ver}
            docker tag python-cg-ci aux.registry.local/python-cg-ci
            docker push aux.registry.local/python-cg-ci

            docker build -f {self.env.project_comm}/docker/Dockerfile.kube-ci -t kube-cg-ci {self.env.monorepo_root} \\
              --build-arg PYTHON_VER_MAJOR={self.env.python_ver_major} \\
              --build-arg PYTHON_VER_MINOR={self.env.python_ver_minor} \\
              --build-arg PYTHON_VER_PATCH={self.env.python_ver_patch} \\
              --build-arg DEBIAN_VER={self.env.debian_ver}
            docker tag kube-cg-ci aux.registry.local/kube-cg-ci
            docker push aux.registry.local/kube-cg-ci

            docker build -f {self.env.project_comm}/docker/Dockerfile.ubuntu-ci -t ubuntu-cg-ci {self.env.monorepo_root}
            docker tag ubuntu-cg-ci aux.registry.local/ubuntu-cg-ci
            docker push aux.registry.local/ubuntu-cg-ci
            """, print_output=True)


def get_current_cluster() -> Citygroves:
    env = import_module(f"env_{environ.str('CG_STAGE')}").Env()

    device = None
    if env.stage in ["local", "test"]:
        device = cluster.Kind(env)

    citygroves = Citygroves(li=Citygroves.Links(device=device),
                            env=env)
    return citygroves


if __name__ == "__main__":
    fire.Fire(get_current_cluster())
