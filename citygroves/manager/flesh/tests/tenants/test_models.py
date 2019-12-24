import pytest


@pytest.mark.django_db
def test_get_lease(sample_application):
    sample_application.save_lease_pdf("/tmp/lease.pdf")
