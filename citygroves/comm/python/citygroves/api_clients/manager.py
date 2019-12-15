import json
from datetime import date
from math import ceil
from typing import List, Dict, Any, Optional

from furl import furl, re
from requests import Session, Response
from requests.adapters import HTTPAdapter
from urllib3 import Retry


from dataclasses import dataclass, asdict, field
from django.core.serializers.json import DjangoJSONEncoder


@dataclass
class Address:
    raw_address: str
    street_line1: Optional[str] = None
    street_line2: Optional[str] = None
    street_line3: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    post_code: Optional[str] = None
    country: Optional[str] = None


@dataclass
class Person:
    first_name: str
    last_name: str
    email: str
    phone: str
    dob: Optional[date] = None


@dataclass
class Referrer:
    first_name: str
    last_name: str
    email: str
    phone: str
    address: Address
    dob: Optional[date] = None


@dataclass
class Application:
    person: Person
    unit_number: int
    room_number: int
    current_address: Address
    number_of_ppl_to_move_in: int
    move_in_date: date
    guarantor_will_pay: bool
    is_employed: bool
    centerlink_will_pay: bool
    have_sufficient_funds: bool
    is_local_student: bool
    is_international_student: bool
    is_young_professional: bool
    referrers: List[Referrer] = field(default_factory=list)
    digital_signature: Optional[str] = None


class Tenants:

    def __init__(self, manager: 'Manager'):
        self._manager = manager
        self._base_url = furl("tenants")

    def create_application(self, application: Application) -> None:
        payload: Dict[str, Any] = asdict(application)
        url = furl(self._base_url).add(path="application/create")
        response: Response = self._manager.post(url, payload)


class Manager:
    def __init__(self, api_url: str):
        self.tenants = Tenants(manager=self)

        self._base_url: furl = furl(api_url)

        self._session = Session()
        self._session.headers = {
            "Content-Type": "application/json; charset=utf-8",
            "Accept": "application/json",
        }

        adapter = HTTPAdapter(max_retries=3)
        self._session.mount("http://", adapter)
        self._session.mount("https://", adapter)

    def post(self, endpoint: furl, data: Dict[str, Any]) -> None:
        url = furl(self._base_url)
        url.add(path=str(endpoint))
        response: Response = self._session.post(url, data=json.dumps(data, cls=DjangoJSONEncoder))
        response.raise_for_status()

    def get(self, endpoint: furl) -> Dict[str, Any]:
        url = furl(self._base_url)
        url.add(path=str(endpoint))
        response: Response = self._session.get(url)
        response.raise_for_status()
        return response.content
