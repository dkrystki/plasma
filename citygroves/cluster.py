from importlib import import_module

from pl.apps.ingress import Ingress
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

        self.system = self.create_namespace("system")
        self.aux = self.create_namespace("aux")
        self.flesh = self.create_namespace("flesh")

        self.system.create_app("ingress", Ingress)
        self.system.create_app("registry", Registry)

        self.aux.create_app("postgresql", Postgres)
        self.aux.create_app("keycloak", Keycloak)
        self.aux.create_app("redis", Redis)

        self.backend = self.flesh.create_app("backend", SkaffoldApp)
        self.appgen = self.flesh.create_app("appgen", SkaffoldApp)
        self.frontend = self.flesh.create_app("frontend", SkaffoldApp)


def get_current_cluster() -> Cluster:
    current_env = import_module(f"env_{environ.str('CG_STAGE')}").Env()
    cluster = Cluster(env=current_env)
    return cluster
