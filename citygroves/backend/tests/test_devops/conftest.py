import os

from citygroves.backend.env_test import BackendEnv
from pytest import fixture


@fixture
def env():
    env = BackendEnv()
    env.activate()
    os.chdir(str(env.root))
    return env
