from datetime import datetime
from typing import List, Dict, Any

import pytest
from django.conf import settings
from django.urls import reverse

from core.models import Photo


@pytest.mark.usefixtures("db", "clean_media")
class TestPhotos:
    @pytest.fixture(autouse=True)
    def setup(self, authenticated_client):
        self.client = authenticated_client

    def test_create(self, sample_photo_payload):
        response = self.client.post(reverse("v1:photos-list"), sample_photo_payload)
        assert response.status_code == 201
        assert Photo.objects.all().count() == 1

    def test_delete(self, sample_photo):
        response = self.client.delete(reverse("v1:photos-detail", kwargs={"pk": sample_photo.pk}))
        assert response.status_code == 204
        assert Photo.objects.all().count() == 0

    def test_put(self, sample_photo, sample_photo_payload):
        sample_photo_payload["name"] = "ChangedName"
        response = self.client.put(reverse("v1:photos-detail", kwargs={"pk": sample_photo.pk}),
                                   sample_photo_payload)
        assert response.status_code == 200
        sample_photo.refresh_from_db()
        assert sample_photo.name == "ChangedName"

    def test_patch(self, sample_photo):
        payload = {"caption": "ChangedCaption"}

        response = self.client.patch(reverse("v1:photos-detail", kwargs={"pk": sample_photo.pk}),
                                     payload)
        assert response.status_code == 200
        sample_photo.refresh_from_db()
        assert sample_photo.caption == "ChangedCaption"

    def test_list(self, photo_factory):
        photo_factory().save()
        photo_factory().save()

        response = self.client.get(reverse("v1:photos-list"))
        assert response.status_code == 200

        data: List[Photo] = response.data
        assert len(data) == 2

    def test_ordering(self, photo_factory):
        newer_photo: Photo = photo_factory()
        older_photo: Photo = photo_factory()

        newer_photo.name = "NewerPhoto"
        newer_photo.publish_date = datetime(2020, 3, 15, 20, 45, 40)
        newer_photo.save()

        older_photo.name = "OlderPhoto"
        older_photo.publish_date = datetime(2020, 3, 12, 20, 45, 40)
        older_photo.save()

        # Test ascending
        asc_url = f'{reverse("v1:photos-list")}?ordering=-publish_date'
        response = self.client.get(asc_url, content_type="application/json")
        assert response.status_code == 200

        data: List[Dict[str, Any]] = response.data
        assert data[0]["name"] == newer_photo.name
        assert data[1]["name"] == older_photo.name

        # Test descending
        desc_url = f'{reverse("v1:photos-list")}?ordering=publish_date'
        response = self.client.get(desc_url, content_type="application/json")
        assert response.status_code == 200

        data: List[Dict[str, Any]] = response.data
        assert data[0]["name"] == older_photo.name
        assert data[1]["name"] == newer_photo.name

    def test_filtering(self, photo_factory, user_factory):
        photo1: Photo = photo_factory()
        photo2: Photo = photo_factory()

        photo1.user = user_factory("TestUser1")
        photo1.save()

        photo2.user = user_factory("TestUser2")
        photo2.save()

        url = f'{reverse("v1:photos-list")}?search={photo1.user.username}'
        response = self.client.get(url, content_type="application/json")
        assert response.status_code == 200

        data: List[Dict[str, Any]] = response.data
        assert len(data) == 1
        assert data[0]["username"] == photo1.user.username

    def test_image_resized(self, sample_image_factory, sample_photo_payload):
        sample_photo_payload["image"] = sample_image_factory(2024, 2024)

        response = self.client.post(reverse("v1:photos-list"), sample_photo_payload)
        assert response.status_code == 201

        photo = Photo.objects.first()
        assert photo.thumbnail.width == settings.IMAGE_SERVE_SIZE[0]
        assert photo.thumbnail.height == settings.IMAGE_SERVE_SIZE[1]
