import json
import pytest

from tenants.models import Application
from tenants.serializers import ApplicationSerializer


@pytest.mark.django_db
def test_serializer(create_rooms, application_payload):

    serializer = ApplicationSerializer(data=application_payload)
    serializer.is_valid(raise_exception=True)
    serializer.save()

    assert Application.objects.all().count() == 1
