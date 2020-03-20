import os
import pl.devops

from loguru import logger


class Graylog(pl.devops.App):
    class Sets(pl.devops.App.Sets):
        pass

    class Links(pl.devops.App.Links):
        pass

    def __init__(self, se: Sets, li: Links):
        super().__init__(se, li)

    def seed(self) -> None:
        os.chdir(str(self.se.app_root))

        logger.info("🌱Seeding graylog")

        mongo_pod: str = self.li.namespace.kubectl('get pods -l app=mongodb-replicaset '
                                           '-o name | grep -m 1 -o "graylog-graylog-mongodb.*$"')
        self.li.namespace.kubectl(f'exec {mongo_pod} -- bash -c "mkdir -p /home/restore"')
        self.li.namespace.kubectl(f'cp dump {mongo_pod}:home/restore/graylog')
        self.li.namespace.kubectl(f'exec {mongo_pod} -- bash -c "mongorestore --quiet /home/restore"')

        logger.info("👌Seeding graylog done")

    def dump_data(self) -> None:
        os.chdir(str(self.se.app_root))

        logger.info("♻️Dumping graylog♻")

        mongo_pod: str = self.li.namespace.kubectl('get pods -l app=mongodb-replicaset '
                                           '-o name | grep -m 1 -o "graylog-graylog-mongodb.*$"')
        self.li.namespace.kubectl(f'exec {mongo_pod} -- bash -c "mongodump --quiet -d graylog -o /home/dumps"')
        self.li.namespace.kubectl(f'cp {mongo_pod}:home/dumps/graylog dump')
        logger.info("♻️Dumping graylog done\n")

    def deploy(self) -> None:
        super().deploy()

        self.li.namespace.helm("graylog").install("stable/graylog", "1.3.9")
        self.li.namespace.kubectl("apply -f k8s/fluentbit-configmap.yaml")
        self.li.namespace.helm("fluentbit").install("stable/fluent-bit", "2.8.2")
        self.seed()

    def delete(self) -> None:
        super().delete()

        self.li.namespace.helm("graylog").delete()
