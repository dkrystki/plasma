#!/usr/bin/env python
from pathlib import Path
import os

from kubernetes.stream import stream
from loguru import logger

from shangren.utils.deploy import run, kube


def deploy() -> None:
    os.chdir(Path(__file__).absolute().parent)
    logger.info("🚀Deploying bitstamp.")

    logger.info("🚀Creating sql database.")
    postgres_pod: str = next(
        p.metadata.name for p in kube.list_namespaced_pod("mockexchs").items if "postgres" in p.metadata.name)

    exec_command = [
        '/bin/bash', '-c',
        """
            PGUSER=postgres PGPASSWORD=password psql <<- EOSQL
            CREATE USER bitstamp WITH PASSWORD 'password';
            CREATE DATABASE bitstamp;
            GRANT ALL PRIVILEGES ON DATABASE bitstamp TO bitstamp;
            ALTER DATABASE bitstamp OWNER TO bitstamp;
            EOSQL
        """]
    resp = stream(kube.connect_get_namespaced_pod_exec, postgres_pod, "mockexchs",
                  command=exec_command,
                  stderr=True, stdin=False,
                  stdout=True, tty=True)
    logger.info("👌Created sql database.")
    logger.info("👌Deployed bitstamp.\n")


if __name__ == "__main__":
    deploy()
