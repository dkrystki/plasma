import os

from pytest import fixture
from plasma.hmlet.env_test import HmletEnv


@fixture
def env():
    env = HmletEnv()
    env.activate()
    os.chdir(str(env.root))
    return env
