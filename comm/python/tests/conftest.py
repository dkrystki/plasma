import os

from pytest import fixture
from plasma.env import PlasmaEnv


@fixture
def env():
    env = PlasmaEnv()
    env.activate()
    os.chdir(str(env.root))
    return env

