import os
from dataclasses import dataclass

from pl.apps import App

from loguru import logger


class Sentry(App):
    @dataclass
    class Sets(App.Sets):
        pass

    @dataclass
    class Links(App.Links):
        pass

    def __init__(self, se: Sets, li: Links):
        super().__init__(se, li)

    def dump_data(self) -> None:
        os.chdir(str(self.se.app_root))

        logger.info("♻️Dumping sentry")

        namespace = self.li.namespace
        sentry_pod: str = namespace.kubectl('get pods -l role=web -o name | grep -m 1 -o "sentry-web.*$"')
        namespace.kubectl(f'exec {sentry_pod} -- bash -c "sentry export --silent --indent=2 '
                       f'--exclude migrationhistory,permission,savedsearch,contenttype > /home/sentry/dump.json"')
        namespace.kubectl(f'cp {sentry_pod}:home/sentry/dump.json dump.json')
        logger.info("♻️Dumping sentry done\n")

    def seed(self) -> None:
        os.chdir(str(self.se.app_root))

        logger.info("🌱Seeding sentry")

        namespace = self.li.namespace
        sentry_pod: str = namespace.kubectl('get pods -l role=web -o name | grep -m 1 -o "sentry-web.*$"')
        namespace.kubectl(f'cp dump.json {sentry_pod}:home/sentry/dump.json')
        namespace.kubectl(f'exec {sentry_pod} -- bash -c "sentry django loaddata /home/sentry/dump.json"')

        logger.info("👌Seeding sentry done")

    def deploy(self) -> None:
        super().deploy()

        logger.info("🚀Deploying sentry")
        self.li.namespace.helm("sentry").install("stable/sentry", "3.1.5")
        self.seed()
        logger.info("👌Deployed sentry\n")

    def delete(self) -> None:
        super().delete()

        self.li.namespace.helm("sentry").delete()
