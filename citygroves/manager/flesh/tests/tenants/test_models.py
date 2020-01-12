import pytest

from tenants.models import Person


@pytest.mark.usefixtures("db")
class TestApplication:
    def test_get_lease(self, sample_application):
        sample_application.save_lease_pdf("/tmp/lease.pdf")


@pytest.mark.usefixtures("db")
class TestTenant:
    def test_str_representation(self, sample_tenant):
        person1: Person = sample_tenant.people.all()[0]
        person2: Person = sample_tenant.people.all()[1]

        person1.first_name = "FirstName1"
        person1.middle_names = "MidName11 MidName12"
        person1.last_name = "LastName1"
        person1.save()

        person2.first_name = "FirstName2"
        person2.middle_names = "MidName12 MidName12"
        person2.last_name = "LastName2"
        person2.save()

        assert str(sample_tenant) == "FirstName1 MidName11 MidName12 LastName1 & FirstName2 MidName12 MidName12 LastName2"
