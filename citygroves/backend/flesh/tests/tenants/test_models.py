from pathlib import Path

import pytest


@pytest.mark.usefixtures("db")
class TestApplication:
    def test_get_lease(self, sample_application):
        sample_application.save_lease_pdf(Path("/tmp/lease.pdf"))


@pytest.mark.usefixtures("db")
class TestTenant:
    def test_str_representation(self, sample_tenant):
        from tenants.models import Person

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

        str_repr = "FirstName1 MidName11 MidName12 LastName1 and FirstName2 MidName12 MidName12 LastName2"
        assert str(sample_tenant) == str_repr


@pytest.mark.usefixtures("db")
class TestEntryNotice:
    def test_create_entry_notice(self, sample_entry_notice):
        sample_entry_notice.create_pdf(path=Path("/tmp/entry-notice.pdf"))
