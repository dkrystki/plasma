#!/usr/bin/env python3
import fire

from dataclasses import dataclass
from importlib import import_module

from hmlet.env_comm import HmletEnvComm
from hmlet.photos.app import Photos
from pl.apps import PythonUtils

from pl.apps.minio import Minio
from pl.apps.postgres import Postgres
from pl import cluster
from pl.devops import run

import environ

environ = environ.Env()


class Hmlet(cluster.Cluster):
    @dataclass
    class Links(cluster.Cluster.Links):
        pass

    @dataclass
    class Sets(cluster.Cluster.Sets):
        pass

    def __init__(self, li: Links, se: Sets, env: HmletEnvComm):
        super().__init__(li, se, env)

        self.env = env

        self.python = PythonUtils(se=PythonUtils.Sets(),
                                  li=PythonUtils.Links(env=self.env))

        self.aux = self.create_namespace("aux")
        self.flesh = self.create_namespace("flesh")

        self.aux.create_app("postgresql", Postgres)
        self.aux.create_app("minio", Minio)

        self.photos: Photos = self.flesh.create_app("photos", Photos)

    def install_deps(self) -> None:
        super().install_deps()
        self.install_hostess()
        self.install_kubectl()
        self.install_helm()
        self.install_skaffold()
        self.install_kind()

    def bootstrap_local_dev(self) -> None:
        self.install_deps()
        self.photos.python.bootstrap_local_dev()

        self.prebuild_all()

    def add_hosts(self):
        super().add_hosts()

        cluster_ip = self.li.device.get_ip()

        run(f"""
            {self.sudo()} hostess add {self.env.photos.address} {cluster_ip}
            {self.sudo()} hostess add {self.env.registry.address} {cluster_ip}
            {self.sudo()} hostess add {self.env.minio.address} {cluster_ip}
            """)

    def prebuild_all(self):
        super().prebuild_all()
        self.photos.docker.prebuild()

    def build_ci_images(self):
        run(f"""
            docker login aux.registry.local --username {self.env.aux.registry.username} \\
                -p{self.env.aux.registry.password}

            docker build -f {self.env.comm}/docker/Dockerfile.python-ci \\
              -t python-ht-ci {self.env.plasma.root} \\
              --build-arg PYTHON_VER_MAJOR={self.env.python.ver_major} \\
              --build-arg PYTHON_VER_MINOR={self.env.python.ver_minor} \\
              --build-arg PYTHON_VER_PATCH={self.env.python.ver_patch} \\
              --build-arg DEBIAN_VER={self.env.debian_ver}
            docker tag python-ht-ci {self.env.aux.registry.address}/python-ht-ci
            docker push {self.env.aux.registry.address}/python-ht-ci

            docker build -f {self.env.comm}/docker/Dockerfile.kube-ci -t kube-ht-ci {self.env.plasma.root} \\
              --build-arg PYTHON_VER_MAJOR={self.env.python.ver_major} \\
              --build-arg PYTHON_VER_MINOR={self.env.python.ver_minor} \\
              --build-arg PYTHON_VER_PATCH={self.env.python.ver_patch} \\
              --build-arg DEBIAN_VER={self.env.debian_ver}
            docker tag kube-ht-ci {self.env.aux.registry.address}/kube-ht-ci
            docker push {self.env.aux.registry.address}/kube-ht-ci
            """, print_output=True)


def get_current_cluster() -> Hmlet:
    env = import_module(f"plasma.hmlet.env_{environ.str('HT_STAGE')}").HmletEnv()

    device = None
    if env.stage in ["local", "test"]:
        device = cluster.Kind(env)

    hmlet = Hmlet(li=Hmlet.Links(device=device),
                  se=Hmlet.Sets(deploy_ingress=True),
                  env=env)
    return hmlet


if __name__ == "__main__":
    fire.Fire(get_current_cluster())
