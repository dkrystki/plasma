from datetime import date, datetime

import factory

from housing.models import Room
from tenants import models


class PersonFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.Person

    first_name = "Josh"
    last_name = "Arystoteles"
    email = "josh.test@gmail.com"
    dob = datetime(1995, 1, 3)
    phone = "123123123"


class TenantFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.Tenant

    @factory.post_generation
    def people(self, create, extracted, **kwargs):
        if create:
            self.people.add(PersonFactory())
            self.people.add(PersonFactory())
            return

        if extracted:
            for people in extracted:
                self.people.add(people)

    room = factory.LazyAttribute(lambda o: Room.objects.get(id=1))


class EntryNoticeFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.EntryNotice

    tenant = factory.SubFactory(TenantFactory)
    planned_on = date(2020, 2, 14)
    planned_time = "10am - 2pm"
    is_inspection = True
    is_cleaning = False
    is_repairs_or_maintenance = False
    is_pest_control = False
    is_showing_to_buyer = False
    is_valutation = False
    is_fire_and_rescue = False


class AddressFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.Address

    street_line1 = "Australian street line1"
    street_line2 = "Australian street line2"
    street_line3 = "Australian street line3"
    city = "Brisbane"
    state = "QLD"
    country = "Australia"
    post_code = "1234"
    raw_address = "Australian street line1, Australian street line2, Australian street line3 \n Australia Brisbane QLD"


class ReferrerFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.Referrer

    first_name = "Josh"
    last_name = "Arystoteles"
    email = "josh.test@gmail.com"
    phone = "123123123"
    address = factory.SubFactory(AddressFactory)


class ApplicationFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.Application

    person = factory.SubFactory(PersonFactory)
    room = factory.LazyAttribute(lambda o: Room.objects.get(id=1))
    current_address = factory.SubFactory(AddressFactory)
    number_of_ppl_to_move_in = 1
    move_in_date = datetime(2019, 8, 22)
    guarantor_will_pay = True
    centerlink_will_pay = False
    is_employed = True
    have_sufficient_funds = False
    is_local_student = False
    is_international_student = False
    is_young_professional = True

    @factory.post_generation
    def referrers(self, create, extracted, **kwargs):
        if create:
            self.referrers.add(ReferrerFactory(applicant=self.person))
            self.referrers.add(ReferrerFactory(applicant=self.person))
            return

        if extracted:
            for referrer in extracted:
                self.referrers.add(referrer)

    digital_signature = None
