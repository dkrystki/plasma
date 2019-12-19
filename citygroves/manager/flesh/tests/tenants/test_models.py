import json

import pytest
from django.urls import reverse

from tenants.models import Application
from tenants.serializers import ApplicationSerializer


@pytest.mark.django_db
def test_get_lease(sample_application):
    sample_application.save_lease_pdf("/tmp/lease.pdf")

