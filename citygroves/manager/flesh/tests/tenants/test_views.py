import pytest
from django.urls import reverse

from tenants.models import Application


@pytest.mark.usefixtures("db", "create_rooms")
class TestApplicant:
    @pytest.fixture(autouse=True)
    def setup(self, client):
        self.client = client

    def test_create(self, sample_application_payload):
        response = self.client.post(reverse("tenants:application-list"), sample_application_payload,
                                    content_type='application/json')
        assert response.status_code == 201
        assert Application.objects.all().count() == 1

    def test_put(self, sample_application, sample_application_payload):
        sample_application_payload["person"]["first_name"] = "Changed"
        sample_application_payload["current_address"]["city"] = "NewCity"
        sample_application_payload["is_employed"] = True
        sample_application_payload["referrers"][1]["first_name"] = "NewName"
        response = self.client.put(reverse("tenants:application-detail", kwargs={"pk": sample_application.pk}),
                                   data=sample_application_payload,
                                   content_type='application/json')
        assert response.status_code == 200
        sample_application.refresh_from_db()
        assert sample_application.person.first_name == "Changed"
        assert sample_application.current_address.city == "NewCity"
        assert sample_application.is_employed
        assert sample_application.referrers.all()[1].first_name == "NewName"

    def test_patch(self, sample_application):
        payload = {
            "person": {
                "first_name": "Changed",
            },
            "current_address": {
                "city": "NewCity"
            },
            "is_employed": True
        }

        response = self.client.patch(reverse("tenants:application-detail", kwargs={"pk": sample_application.pk}),
                                     data=payload,
                                     content_type='application/json')
        assert response.status_code == 200
        sample_application.refresh_from_db()
        assert sample_application.person.first_name == "Changed"
        assert sample_application.current_address.city == "NewCity"
        assert sample_application.is_employed

    def test_list(self, application_factory):
        app1 = application_factory()
        app2 = application_factory()

        response = self.client.get(reverse("tenants:application-list"), content_type='application/json')
        assert response.status_code == 200
        assert len(response.data.serializer.instance) == 2


@pytest.mark.usefixtures("db")
class TestPerson:
    @pytest.fixture(autouse=True)
    def setup(self, client):
        self.client = client

    def test_get(self, sample_person):
        response = self.client.get(reverse("tenants:people-detail", kwargs={"pk": sample_person.pk}),
                                   content_type='application/json')
        assert response.status_code == 200
        sample_person.refresh_from_db()
        assert sample_person.first_name == response.data["first_name"]

    def test_patch(self, sample_person):
        response = self.client.patch(reverse("tenants:people-detail", kwargs={"pk": sample_person.pk}),
                                     {"first_name": "NewName"},
                                     content_type='application/json')
        assert response.status_code == 200
        sample_person.refresh_from_db()
        assert sample_person.first_name == "NewName"

    def test_put(self, sample_person, sample_person_payload):
        sample_person_payload["first_name"] = "NewName"
        response = self.client.put(reverse("tenants:people-detail", kwargs={"pk": sample_person.pk}),
                                   sample_person_payload,
                                   content_type='application/json')
        assert response.status_code == 200
        sample_person.refresh_from_db()
        assert sample_person.first_name == "NewName"

    def test_list(self, person_factory):
        person1 = person_factory()
        person2 = person_factory()

        response = self.client.get(reverse("tenants:people-list"), content_type='application/json')
        assert response.status_code == 200
        assert len(response.data.serializer.instance) == 2


@pytest.mark.usefixtures("db")
class TestTenant:
    @pytest.fixture(autouse=True)
    def setup(self, client):
        self.client = client

    def test_get(self, sample_tenant):
        response = self.client.get(reverse("tenants:tenants-detail", kwargs={"pk": sample_tenant.pk}),
                                   content_type='application/json')
        assert response.status_code == 200
        sample_tenant.refresh_from_db()
        assert response.data["str_repr"] == str(sample_tenant)
        assert sample_tenant.people.all()[0].first_name == response.data["people"][0]["first_name"]

    def test_patch(self, sample_tenant):
        response = self.client.patch(reverse("tenants:tenants-detail", kwargs={"pk": sample_tenant.pk}),
                                     {"people": [{"first_name": "NewName1"},
                                                 {"first_name": "NewName2"}],
                                      "room_number": 2,
                                      "unit_number": 5},
                                     content_type='application/json')
        assert response.status_code == 200
        sample_tenant.refresh_from_db()
        assert sample_tenant.people.all()[0].first_name == "NewName1"
        assert sample_tenant.people.all()[1].first_name == "NewName2"
        assert sample_tenant.room.number == 2
        assert sample_tenant.room.unit.number == 5

    def test_put(self, sample_tenant, sample_tenant_payload):
        sample_tenant_payload["people"][0]["first_name"] = "NewName1"
        sample_tenant_payload["people"][1]["first_name"] = "NewName2"
        sample_tenant_payload["room_number"] = 4
        sample_tenant_payload["unit_number"] = 8
        response = self.client.put(reverse("tenants:tenants-detail", kwargs={"pk": sample_tenant.pk}),
                                   sample_tenant_payload,
                                   content_type='application/json')
        assert response.status_code == 200
        sample_tenant.refresh_from_db()
        assert sample_tenant.people.all()[0].first_name == "NewName1"
        assert sample_tenant.people.all()[1].first_name == "NewName2"
        assert sample_tenant.room.number == 4
        assert sample_tenant.room.unit.number == 8

    def test_list(self, create_rooms, tenant_factory):
        person1 = tenant_factory()
        person2 = tenant_factory()

        response = self.client.get(reverse("tenants:tenants-list"), content_type='application/json')
        assert response.status_code == 200
        assert len(response.data) == 2


@pytest.mark.usefixtures("db")
class TestAddress:

    @pytest.fixture(autouse=True)
    def setup(self, client):
        self.client = client

    def test_get(self, sample_address):
        response = self.client.get(reverse("tenants:addresses-detail", kwargs={"pk": sample_address.pk}),
                                   content_type='application/json')
        assert response.status_code == 200
        sample_address.refresh_from_db()
        assert sample_address.street_line1 == response.data["street_line1"]

    def test_patch(self, sample_address):
        response = self.client.patch(reverse("tenants:addresses-detail", kwargs={"pk": sample_address.pk}),
                                     {"street_line1": "NewStreet"},
                                     content_type='application/json')
        assert response.status_code == 200
        sample_address.refresh_from_db()
        assert sample_address.street_line1 == "NewStreet"

    def test_put(self, sample_address, sample_address_payload):
        sample_address_payload["street_line1"] = "NewStreet"
        response = self.client.put(reverse("tenants:addresses-detail", kwargs={"pk": sample_address.pk}),
                                   sample_address_payload,
                                   content_type='application/json')
        assert response.status_code == 200
        sample_address.refresh_from_db()
        assert sample_address.street_line1 == "NewStreet"

    def test_list(self, address_factory):
        address1 = address_factory()
        address2 = address_factory()

        response = self.client.get(reverse("tenants:addresses-list"), content_type='application/json')
        assert response.status_code == 200
        assert len(response.data.serializer.instance) == 2


@pytest.mark.usefixtures("db")
class TestReferrers:

    @pytest.fixture(autouse=True)
    def setup(self, client):
        self.client = client

    def test_get(self, sample_referrer):
        response = self.client.get(reverse("tenants:referrers-detail", kwargs={"pk": sample_referrer.pk}),
                                   content_type='application/json')
        assert response.status_code == 200
        sample_referrer.refresh_from_db()
        assert sample_referrer.first_name == response.data["first_name"]

    def test_patch(self, sample_referrer):
        response = self.client.patch(reverse("tenants:referrers-detail", kwargs={"pk": sample_referrer.pk}),
                                     {
                                         "first_name": "NewName",
                                         "address": {
                                             "street_line1": "NewStreet"
                                         }
                                     },
                                     content_type='application/json')
        assert response.status_code == 200
        sample_referrer.refresh_from_db()
        assert sample_referrer.first_name == "NewName"
        assert sample_referrer.address.street_line1 == "NewStreet"

    def test_put(self, sample_referrer, sample_referrer_payload):
        sample_referrer_payload["first_name"] = "NewName"
        sample_referrer_payload["address"]["street_line1"] = "NewStreet"
        response = self.client.put(reverse("tenants:referrers-detail", kwargs={"pk": sample_referrer.pk}),
                                   sample_referrer_payload,
                                   content_type='application/json')
        assert response.status_code == 200
        sample_referrer.refresh_from_db()
        assert sample_referrer.first_name == "NewName"
        assert sample_referrer.address.street_line1 == "NewStreet"

    def test_list(self, sample_referrer):
        response = self.client.get(reverse("tenants:referrers-list"), content_type='application/json')
        assert response.status_code == 200
        assert len(response.data.serializer.instance) == 2
