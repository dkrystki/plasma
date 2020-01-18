from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Dict, Any, Optional

from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=127)
    middle_names = models.CharField(max_length=127, null=False, blank=True)
    last_name = models.CharField(max_length=127)
    email = models.EmailField(max_length=127, null=True, blank=True)
    dob = models.DateField(max_length=127, null=True)
    phone = models.CharField(max_length=127, null=True, blank=True)


class Address(models.Model):
    street_line1 = models.CharField(max_length=127, null=True, blank=True)
    street_line2 = models.CharField(max_length=127, null=True, blank=True)
    street_line3 = models.CharField(max_length=127, null=True, blank=True)
    city = models.CharField(max_length=127, null=True, blank=True)
    state = models.CharField(max_length=127, null=True, blank=True)
    country = models.CharField(max_length=127, null=True, blank=True)
    post_code = models.CharField(max_length=127, null=True, blank=True)
    raw_address = models.CharField(max_length=512)


class Referrer(models.Model):
    first_name = models.CharField(max_length=127, null=True, blank=True)
    last_name = models.CharField(max_length=127, null=True, blank=True)
    email = models.EmailField(max_length=127, null=True, blank=True)
    phone = models.CharField(max_length=127, null=True, blank=True)
    applicant = models.ForeignKey(Person, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True)


class Application(models.Model):
    from housing.models import Room

    # TODO: handle couples

    person = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True)
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True)
    current_address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True)
    number_of_ppl_to_move_in = models.IntegerField()
    move_in_date = models.DateField()
    guarantor_will_pay = models.BooleanField()
    centerlink_will_pay = models.BooleanField()
    is_employed = models.BooleanField()
    have_sufficient_funds = models.BooleanField()
    is_local_student = models.BooleanField()
    is_international_student = models.BooleanField()
    is_young_professional = models.BooleanField()
    referrers = models.ManyToManyField(Referrer)
    digital_signature = models.ImageField(null=True)

    def save_lease_pdf(self, path: Path) -> None:
        from tenants.tools import LeasePdf
        pdf = LeasePdf()
        input_dict: Dict[str, Any] = {
            "person.full_name": f"{self.person.first_name} {self.person.middle_names} {self.person.last_name}",
            "person.phone": self.person.phone,
            "person.email": self.person.email,
            "unit_address": f"Unit {self.room.unit.number}, 27-29 Herston Road, Kelvin Grove",
            "room.number": self.room.number,
            "starting_on": self.move_in_date,
            "ending_on": "",
            "rent": 150,
            "payment_reference": str(self.room),
            "bond_amount": 300
        }

        pdf.fill(input_dict)
        pdf.save(path)

    def __str__(self):
        return f"{self.person.first_name+self.person.last_name}"


class Tenant(models.Model):
    from housing.models import Room
    people = models.ManyToManyField(Person)
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True)
    lease_start = models.DateField(null=True)
    lease_end = models.DateField(null=True)

    def __str__(self):
        ret = []
        for p in self.people.all():
            ret.append(f"{p.first_name} {p.middle_names} {p.last_name}")

        return " and ".join(ret)


class EntryNotice(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    planned_on = models.DateField(null=False)
    # Time range, "10am - 2pm"
    planned_time = models.CharField(max_length=63, null=False)
    is_inspection = models.BooleanField(null=False, default=True)
    is_cleaning = models.BooleanField(null=False, default=False)
    is_repairs_or_maintenance = models.BooleanField(null=False, default=False)
    is_pest_control = models.BooleanField(null=False, default=False)
    is_showing_to_buyer = models.BooleanField(null=False, default=False)
    is_valutation = models.BooleanField(null=False, default=False)
    is_fire_and_rescue = models.BooleanField(null=False, default=False)

    def __str__(self):
        return f"{str(self.tenant)} Entry Notice"

    def create_pdf(self, path: Path):
        from tenants.tools import EntryNoticePdf

        person1: Person = self.tenant.people.all()[0]
        person2: Person = self.tenant.people.all()[0]
        pdf = EntryNoticePdf()
        input_dict: Dict[str, Any] = {
            "person1.full_name": f"{person1.first_name} {person1.middle_names + ' '}{person1.last_name}",
            "person2.full_name": f"{person2.first_name} {person1.middle_names + ' '}{person2.last_name}",
            "room_number": self.tenant.room.number,
            "unit_number": f"Unit no. {self.tenant.room.unit.number}",
            "planned_on_day_name": self.planned_on.strftime("%A"),
            "planned_on": self.planned_on,
            "planned_time": self.planned_time,
            "issued_on": date.today(),
            "issued_on_day_name": date.today().strftime("%A"),
            "method_of_issue": "email",
            "manager.name": "Shoma Madhoji",
            "is_inspection": self.is_inspection,
            "is_cleaning": self.is_cleaning,
            "is_repairs_or_maintenance": self.is_repairs_or_maintenance,
            "is_pest_control": self.is_pest_control,
            "is_showing_to_buyer": self.is_showing_to_buyer,
            "is_valutation": self.is_valutation,
            "is_fire_and_rescue": self.is_fire_and_rescue,
        }

        pdf.fill(input_dict)
        pdf.save(path)

