from typing import List

from ht.api_clients.photos import Photo


def test_creating_deleting_listing(env, photos_api_client):
    to_del_photos: List[Photo] = photos_api_client.photos.list()

    # delete existing
    for p in to_del_photos:
        photos_api_client.photos.delete(p)

    assert len(photos_api_client.photos.list()) == 0

    photo = Photo(name="TestPhoto",
                  draft=False,
                  caption="Test caption",
                  image=str(env.root / "tests/test_e2e/data/test_image.png"))
    photos_api_client.photos.create(photo)

    photo = Photo(name="TestPhoto2",
                  draft=True,
                  caption="Test caption2",
                  image=str(env.root / "tests/test_e2e/data/test_image.png"))
    photos_api_client.photos.create(photo)

    assert len(photos_api_client.photos.list()) == 2
