import os
from dataclasses import dataclass
from typing import Optional

from pl.devops import run
from pl.apps import App
from pl.kube import HelmRelease
from loguru import logger
from pl.apps.postgres import Postgres


class Keycloak(App):
    @dataclass
    class Sets(App.Sets):
        pass

    @dataclass
    class Links(App.Links):
        postgres: Postgres

    def __init__(self, se: Sets, li: Links):
        super().__init__(se, li)
        self.li = li
        self.helm_release: Optional[HelmRelease] = None

    def deploy(self) -> None:
        super().deploy()

        run("helm repo add codecentric https://codecentric.github.io/helm-charts")
        self.helm_release = self.li.namespace.helm(self.se.name)
        self.helm_release.install("codecentric/keycloak", "7.2.0")
        self.seed()

    def delete(self) -> None:
        super().delete()

        self.li.namespace.helm(self.se.name).delete()

    def dump(self) -> None:
        os.chdir(str(self.se.app_root))

        logger.info("Dumping keycloak database.")

        # TODO: put those credentials to env
        self.li.postgres.master.exec("PGUSER=keycloak PGPASSWORD=password pg_dump -d keycloak > /tmp/dump.sql")
        self.li.postgres.master.copy_from_pod("/tmp/dump.sql", "dumps/dump.sql")
        logger.info("Dumped.")

    def seed(self) -> None:
        os.chdir(str(self.se.app_root))

        logger.info("Restoring keycloak database from dump.")

        self.li.postgres.master.copy_to_pod("dumps/dump.sql", "/tmp/dump.sql")
        self.li.namespace.kubectl(f"scale --replicas=0 -n aux statefulset {self.se.name}")
        # TODO: put those credentials to env
        self.li.postgres.master.exec("PGUSER=postgres PGPASSWORD=password dropdb keycloak")
        self.li.postgres.master.exec("PGUSER=postgres PGPASSWORD=password createdb keycloak")
        self.li.postgres.master.exec("PGUSER=keycloak PGPASSWORD=password psql keycloak -f /tmp/dump.sql")
        self.li.namespace.kubectl(f"scale --replicas=1 -n aux statefulset {self.se.name}")
        logger.info("Restored.")
