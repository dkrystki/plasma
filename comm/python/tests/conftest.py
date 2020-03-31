from pytest import fixture
from plasma.env import Env


@fixture
def env():
    env = Env()
    env.activate()
    return env

