import pytest
from django.urls import reverse

from tenants.models import Application


@pytest.mark.django_db
def test_create_applicant(create_rooms, client, application_payload):
    response = client.post(reverse("tenants:application-list"), application_payload, content_type='application/json')
    assert response.status_code == 201
    assert Application.objects.all().count() == 1


@pytest.mark.django_db
def test_update_get_applicant(create_rooms, client, application_payload):
    response = client.post(reverse("tenants:application-list"), application_payload, content_type='application/json')
    assert response.status_code == 201
    assert Application.objects.all().count() == 1
    application = Application.objects.first()

    response = client.patch(reverse("tenants:application-detail", kwargs={"pk": application.pk}), {"unit_number": 2,
                                                                                                   "is_employed": True},
                            content_type='application/json')
    assert response.status_code == 200

    response = client.get(reverse("tenants:application-detail", kwargs={"pk": application.pk}),
                          content_type='application/json')
    assert response.status_code == 200
    assert response.data.serializer.instance.room.unit.number == 2
    assert response.data.serializer.instance.is_employed


@pytest.mark.django_db
def test_list_applicant(create_rooms, client, application_factory):
    app1 = application_factory()
    app2 = application_factory()

    response = client.get(reverse("tenants:application-list"), content_type='application/json')
    assert response.status_code == 200
    assert len(response.data.serializer.instance) == 2

