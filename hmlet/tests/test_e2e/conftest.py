from pytest import fixture
from ht.api_clients import photos

from plasma.hmlet.env_test import HmletEnv


@fixture
def env() -> HmletEnv:
    env = HmletEnv()
    env.activate()
    return env


@fixture
def photos_api_client(env) -> photos.PhotosApiClient:
    api_client = photos.PhotosApiClient(username="user", password="password",
                                        api_url=f"http://{env.photos.address}/api/v1")
    return api_client
