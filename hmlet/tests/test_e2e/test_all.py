from typing import List

from ht.api_clients.photos import Photo


def test_creating_deleting_listing(env, photos_api_client):
    to_del_photos: List[Photo] = photos_api_client.photos.list()

    # delete existing
    for p in to_del_photos:
        photos_api_client.photos.delete(p)

    assert len(photos_api_client.photos.list()) == 0

    photo_to_create1 = Photo(name="TestPhoto1",
                             draft=False,
                             caption="Test caption1",
                             image=str(env.root / "tests/test_e2e/data/test_image.png"))
    photos_api_client.photos.create(photo_to_create1)

    photo_to_create2 = Photo(name="TestPhoto2",
                             draft=True,
                             caption="Test caption2",
                             image=str(env.root / "tests/test_e2e/data/test_image.png"))
    photos_api_client.photos.create(photo_to_create2)

    fetched_photos: List[Photo] = photos_api_client.photos.list()
    fetched_photo1: Photo = fetched_photos[0]
    assert fetched_photo1.name == photo_to_create1.name

    fetched_photo2: Photo = fetched_photos[1]
    assert fetched_photo2.name == photo_to_create2.name

    assert len(fetched_photos) == 2
