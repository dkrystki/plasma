import os
import responses
from datetime import date


@responses.activate
def test_manager_api_client():
    from citygroves.api_clients.manager import Manager, Application, Person, Address, Referrer

    manager = Manager(os.environ["MANAGER_API_URL"])
    responses.add(responses.POST, f"{os.environ['MANAGER_API_URL']}/application/create", status=201)

    application = Application(person=Person(first_name="test_first_name",
                                            last_name="test_last_name",
                                            email="email",
                                            phone="123123123",
                                            dob=date(1990, 8, 18)),
                              unit_number=1,
                              room_number=1,
                              current_address=Address(street_line1="street 1",
                                                      street_line2="test_2",
                                                      city="Brisbane",
                                                      state="Queensland",
                                                      post_code="123",
                                                      country="Australia",
                                                      raw_address="raw_addrss"),
                              number_of_ppl_to_move_in=1,
                              move_in_date=date(2019, 9, 20),
                              guarantor_will_pay=True,
                              is_employed=True,
                              centerlink_will_pay=False,
                              have_sufficient_funds=False,
                              is_local_student=False,
                              is_international_student=True,
                              is_young_professional=True,
                              referrers=[Referrer(first_name="referref_name",
                                                  last_name="last_name",
                                                  email="test@test.pl",
                                                  phone="123123123",
                                                  dob=date(1990, 8, 18),
                                                  address=Address(raw_address="Australia"))])

    manager.tenants.create_application(application)
