from pytest import fixture
from django.core.management import call_command


@fixture
def application_payload():
    payload = {
        "person": {
            "first_name": "Damian",
            "last_name": "Krystkiewicz",
            "email": "testdf@gmail.au",
            "phone": "112341342",
            "dob": "2020-11-20"
        },

        "unit_number": 1,
        "room_number": 1,

        "current_address": {
            "street_line1": "street 123",
            "street_line2": "street 2 123",
            "street_line3": "vdsds",
            "city": "Brisbane",
            "state": "QLD",
            "post_code": "1231",
            "country": "Australia"
        },
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

        "referrers":
            [
                {
                    "first_name": "Referee",
                    "last_name": "Surname",
                    "email": "referee@gmail.com",
                    "phone": "13223132",
                    "address": {
                        "street_line1": "street 123",
                        "street_line2": "street 2 123",
                        "street_line3": "vdsds",
                        "city": "Brisbane",
                        "state": "QLD",
                        "post_code": "1231",
                        "country": "Australia"
                    },
                },
                {
                    "first_name": "Referee2",
                    "last_name": "Surname",
                    "email": "referee@gmail.com",
                    "phone": "13223132",
                    "address": {
                        "street_line1": "street 123",
                        "street_line2": "street 2 123",
                        "street_line3": "vdsds",
                        "city": "Brisbane",
                        "state": "QLD",
                        "post_code": "1231",
                        "country": "Australia"
                    },
                },
            ]
    }
    return payload


@fixture
def create_rooms():
    call_command('loaddata', 'fixtures/units.yaml', verbosity=0)
    call_command('loaddata', 'fixtures/rooms.yaml', verbosity=0)
