import json

import pytest
from django.urls import reverse

from tenants.models import Application
from tenants.serializers import ApplicationSerializer


@pytest.mark.django_db
def test_create_applicant_view(create_rooms, client, application_payload):
    response = client.post(reverse("tenants:application-create"), application_payload, content_type='application/json')
    assert response.status_code == 201
    assert Application.objects.all().count() == 1
