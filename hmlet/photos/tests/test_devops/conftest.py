import os

from plasma.hmlet.photos.env_test import PhotosEnv
from pytest import fixture


@fixture
def env():
    env = PhotosEnv()
    env.activate()
    os.chdir(str(env.root))
    return env
