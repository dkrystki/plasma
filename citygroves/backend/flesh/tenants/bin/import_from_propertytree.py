#!/usr/bin/env python3
import csv
import os
import re
import sys
from datetime import date
from pathlib import Path
from typing import List, Optional

import click
import dateutil.parser
import django
from django.db import transaction
from tqdm import tqdm

from housing.models import Room
from tenants.models import Person, Tenant

sys.path.append(os.environ["CG_APP_SRC"])


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")

django.setup()


class Importer:
    def __init__(self, input_path: Path):
        self.input_path = input_path

    def _create_person(self, tenancy: str, email: str):
        middle_names = ""
        if len(tenancy.split()) > 2:
            middle_names = " ".join(tenancy.split()[1:-1])

        person = Person(
            first_name=tenancy.split()[0],
            middle_names=middle_names,
            last_name=tenancy.split()[-1],
            email=email if email else None,
        )
        person.save()
        return person

    def start(self):
        with open(str(self.input_path), newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in tqdm(reader):
                people: List[Person] = []

                # Handle multiple tenants in one room
                if " and " in row["Tenancy"]:
                    tenancy0: str = row["Tenancy"].split(" and ")[0]
                    tenancy1: str = row["Tenancy"].split(" and ")[1]
                    email0: Optional[str] = None
                    email1: Optional[str] = None
                    if row["Email"]:
                        email0 = row["Email"].split(",")[0].strip()
                        email1 = row["Email"].split(",")[1].strip()

                    people.append(self._create_person(tenancy0, email0))
                    people.append(self._create_person(tenancy1, email1))
                else:
                    people.append(self._create_person(row["Tenancy"], row["Email"]))

                unit_n: int = int(list(filter(None, re.split("[U,R,/]", row["Property"])))[0])
                room_n: int = int(list(filter(None, re.split("[U,R,/]", row["Property"])))[1])

                room = Room.objects.get(number=room_n, unit__number=unit_n)

                lease_start: date = dateutil.parser.parse(row["Lease Start"])
                lease_end: date = dateutil.parser.parse(row["Lease End"])

                tenant = Tenant(room=room, lease_start=lease_start, lease_end=lease_end)
                tenant.save()
                tenant.people.set(people)
                tenant.save()


@click.command()
@click.argument("input_path", type=str)
@transaction.atomic
def import_from_propertytree(input_path: str):
    importer = Importer(Path(input_path))
    importer.start()


if __name__ == "__main__":
    import_from_propertytree()
