from functools import partial
from io import BytesIO
from pathlib import Path
from typing import Dict, Any, List

from core.models import Photo
from django.conf import settings
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from pytest import fixture
from PIL import Image

from rest_framework import status
from rest_framework.test import APIClient
from tests.factories.app import PhotoFactory


password = "password"


@fixture
def user_factory():
    def factory(username: str) -> User:
        user = User.objects.create_user(username=username, password=password)
        return user

    return factory


@fixture
def test_user(db, user_factory) -> User:
    username = "TestUser"
    try:
        return User.objects.get(username=username, password=password)
    except User.DoesNotExist:
        user = user_factory(username)
        user.is_active = True
        user.save()
        return user


@fixture
def authenticated_client(test_user, client) -> APIClient:

    auth_client = APIClient()

    resp = client.post(reverse("token_obtain_pair"), {'username': test_user.username,
                                                      'password': password}, format='json')
    assert resp.status_code == status.HTTP_200_OK
    token = resp.json()['access']

    auth_client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
    return auth_client


@fixture
def sample_image_factory():
    def factory(size_x: int, size_y: int) -> Image:
        img_data = BytesIO()
        image = Image.new('RGB', size=(size_x, size_y), color=(255, 0, 0, 0))
        image.save(img_data, format='JPEG')
        image_name = 'TestImage'
        image = SimpleUploadedFile(
            image_name + '.jpg', img_data.getvalue(), 'image/jpg')
        return image
    return factory


@fixture
def sample_photo_payload(sample_image_factory) -> Dict[str, Any]:

    return {
        "name": "TestPhoto",
        "draft": False,
        "caption": "TestCaption",
        "image": sample_image_factory(128, 128),
        "publish_date": "2020-3-22T19:50:08"
    }


@fixture
def many_photo_payloads(sample_image_factory) -> List[Dict[str, Any]]:
    return [
        {
            "name": "TestPhoto",
            "draft": False,
            "caption": "TestCaption",
            "image": sample_image_factory(128, 128),
            "publish_date": "2020-3-22T19:50:08"
        },
        {
            "name": "TestPhoto2",
            "draft": True,
            "caption": "TestCaption2",
            "image": sample_image_factory(128, 128),
            "publish_date": "2020-3-22T19:50:08"
        }
    ]


@fixture
def photo_factory(test_user, sample_image_factory) -> partial:
    return partial(PhotoFactory, user=test_user, image=sample_image_factory(128, 128))


@fixture
def sample_photo(photo_factory) -> Photo:
    photo = photo_factory()
    photo.save()
    return photo


@fixture
def clean_media():
    yield
    media = Path(settings.MEDIA_ROOT)

    for f in media.glob("*.jpg"):
        f.unlink()
