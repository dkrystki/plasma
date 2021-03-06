import os
from pathlib import Path

import pytest_factoryboy
from django.core.management import call_command
from pytest import fixture

import tests.factories.tenants

pytest_factoryboy.register(tests.factories.tenants.PersonFactory)
pytest_factoryboy.register(tests.factories.tenants.TenantFactory)
pytest_factoryboy.register(tests.factories.tenants.AddressFactory)
pytest_factoryboy.register(tests.factories.tenants.ReferrerFactory)
pytest_factoryboy.register(tests.factories.tenants.ApplicationFactory)
pytest_factoryboy.register(tests.factories.tenants.EntryNoticeFactory)


@fixture
def sample_person_payload():
    return {
        "first_name": "Damian",
        "last_name": "Krystkiewicz",
        "email": "testdf@gmail.au",
        "phone": "112341342",
        "dob": "1990-11-20",
    }


@fixture
def sample_tenant_payload(sample_person_payload):
    return {
        "people": [dict(sample_person_payload), dict(sample_person_payload)],
        "room_number": 6,
        "unit_number": 5,
        "lease_start": "2020-11-20",
        "lease_end": "2021-11-20",
    }


@fixture
def sample_entry_notice_payload():
    return {
        "tenant": 1,
        "planned_on": "2020-11-20",
        "planned_time": "10am - 2pm",
        "is_inspection": True,
        "is_cleaning": False,
        "is_repairs_or_maintenance": False,
        "is_pest_control": False,
        "is_showing_to_buyer": False,
        "is_valutation": False,
        "is_fire_and_rescue": False,
    }


@fixture
def sample_address_payload():
    return {
        "street_line1": "Australian street line1",
        "street_line2": "Australian street line2",
        "street_line3": "Australian street line3",
        "city": "Brisbane",
        "state": "QLD",
        "post_code": "1234",
        "country": "Australia",
        "raw_address": "Australian street line1, Australian street line2, "
        "Australian street line3 \n Australia Brisbane QLD",
    }


@fixture
def sample_referrer_payload(sample_address_payload):
    return {
        "first_name": "Referee2",
        "last_name": "Surname",
        "email": "referee@gmail.com",
        "phone": "13223132",
        "address": sample_address_payload,
    }


@fixture
def sample_application_payload(sample_person_payload, sample_address_payload, sample_referrer_payload):
    payload = {
        "person": sample_person_payload,
        "unit_number": 1,
        "room_number": 1,
        "current_address": sample_address_payload,
        "number_of_ppl_to_move_in": 1,
        "move_in_date": "2020-11-20",
        "guarantor_will_pay": True,
        "is_employed": False,
        "centerlink_will_pay": False,
        "have_sufficient_funds": True,
        "is_local_student": False,
        "is_international_student": True,
        "is_young_professional": False,
        "digital_signature": None,
        "referrers": [dict(sample_referrer_payload), dict(sample_referrer_payload)],
    }
    return payload


@fixture
def create_rooms():
    call_command("loaddata", "../../housing/fixtures/units.yaml", verbosity=0)
    call_command("loaddata", "../../housing/fixtures/rooms.yaml", verbosity=0)


@fixture
def sample_application(create_rooms, application_factory):
    application = application_factory()
    return application


@fixture
def sample_person(person_factory):
    person = person_factory()
    return person


@fixture
def sample_tenant(create_rooms, tenant_factory):
    tenant = tenant_factory()
    return tenant


@fixture
def sample_entry_notice(create_rooms, entry_notice_factory):
    entry_notice = entry_notice_factory()
    return entry_notice


@fixture
def sample_address(address_factory):
    address = address_factory()
    return address


@fixture
def sample_referrer(sample_application):
    referrer = sample_application.referrers.all()[0]
    return referrer


@fixture
def data_dir():
    return Path(os.path.dirname(os.path.realpath(__file__))) / "data"
