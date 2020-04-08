import os

from pytest import fixture
from plasma.citygroves.env_test import CitygrovesEnv


@fixture
def env():
    env = CitygrovesEnv()
    env.activate()
    os.chdir(str(env.root))
    return env
