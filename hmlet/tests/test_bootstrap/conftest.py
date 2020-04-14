from typing import List

import pl.devops
from pytest import fixture
from hmlet.env_test import HmletEnv

import environ

environ = environ.Env()

env = HmletEnv()


class Container:
    container_name = "hmlet-bootstrap-test"

    def __init__(self):
        pass

    @env.in_project_root
    def build(self):
        pl.devops.run(f"docker build -f tests/test_bootstrap/Dockerfile -t {self.container_name} {env.monorepo_root}",
                      print_output=True)

    @env.in_project_root
    def start(self) -> None:
        self.stop()
        pl.devops.run(f"docker run -d --name {self.container_name} {self.container_name} ",
                      print_output=True)

    def run(self, commands: List[str]) -> None:
        command_str = " && ".join([f"{c}" for c in commands])
        pl.devops.run(f"""docker exec {self.container_name} bash -c '{command_str}' """, print_output=True)

    def stop(self) -> None:
        pl.devops.run(f"docker stop {self.container_name}", ignore_errors=True)
        pl.devops.run(f"docker rm {self.container_name}", ignore_errors=True)


@fixture
def container():
    cont = Container()
    cont.build()
    cont.start()
    return cont
