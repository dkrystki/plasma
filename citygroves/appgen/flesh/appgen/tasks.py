import base64
from datetime import datetime, date
from typing import Dict, Any, List
import re

from appgen.celer import app
from loguru import logger
from django.conf import settings
from googleapiclient.discovery import build, Resource
from google.oauth2.credentials import Credentials

from commonregex import CommonRegex


class Fetcher:
    def __init__(self) -> None:
        # client_config: Dict[str, Any] = {
        #     "installed": {
        #         "client_id": settings.GMAIL.CLIENT_ID,
        #         "client_secret": settings.GMAIL.CLIENT_SECRET,
        #         "redirect_uris": ["urn:ietf:wg:oauth:2.0:oob"],
        #         "auth_uri": settings.GMAIL.GOOGLE_AUTH_URI,
        #         "token_uri": settings.GMAIL.GOOGLE_TOKEN_URI,
        #     }
        # }
        #
        # flow: InstalledAppFlow = InstalledAppFlow.from_client_config(client_config,
        #                                         scopes=['https://mail.google.com/'])
        # creds: Credentials = flow.run_local_server(port=0)

        self.creds: Credentials = Credentials(
            None,
            refresh_token='1//0g_HVOsbpO8C8CgYIARAAGBASNwF-L9Ir2eMZbyB9gZBQFcJIwgUQ6JxqCoAiSUQqf-4sHFg2xnTN7-p0rXDQ_-o8QC_IVZ02gqA',
            token_uri=settings.GMAIL.GOOGLE_TOKEN_URI,
            client_id=settings.GMAIL.CLIENT_ID,
            client_secret=settings.GMAIL.CLIENT_SECRET,
        )
        self.user_id: str = settings.GMAIL.OWNER_EMAIL

    def build_payload(self, mail_body: str) -> Dict[str, Any]:
        values = [s.strip() for s in re.split(r"\*.*?\*", mail_body, flags=re.DOTALL) if s]

        yes_no_to_bool = lambda x: {"yes": True, "no": False}[x]

        payload = {
            "person": {
                "first_name": values[0].split()[0],
                "last_name": values[0].split()[1],
                "email": values[1],
                "phone": values[2],
                "dob": datetime.strptime(values[3], "%m/%d/%Y").date()
            },
            "room": {
                "unit": values[4],
                "number": values[5]
            },
            "current_address": self._build_address(values[6]),
            "number_of_ppl_to_move_in": values[7],
            "move_in_date": datetime.strptime(values[8], "%m/%d/%Y").date(),
            "guarantor_will_pay": yes_no_to_bool(values[13]),
            "is_employed": yes_no_to_bool(values[14]),
            "centerlink_will_pay": yes_no_to_bool(values[15]),
            "have_sufficient_funds": yes_no_to_bool(values[16]),
            "is_local_student": yes_no_to_bool(values[18]),
            "is_international_student": yes_no_to_bool(values[19]),
            "is_young_professional": yes_no_to_bool(values[20]),

            "referrers":
                [
                    {
                        "first_name": values[23].split()[0] if len(values[23].split()) > 1 else None,
                        "last_name": values[23].split()[1] if len(values[23].split()) > 2 else None,
                        "email": values[25] if values[25] else None,
                        "phone": values[26] if values[25] else None,
                        "address": self._build_address(values[27]),
                    },
                    {
                        "first_name": values[23].split()[0] if len(values[29].split()) > 1 else None,
                        "last_name": values[23].split()[1] if len(values[29].split()) > 2 else None,
                        "email": values[33],
                        "phone": values[32],
                        "address": self._build_address(values[31]),
                    }
                ]
        }

        return payload

    def fetch_all(self) -> None:
        service: Resource = build('gmail', 'v1', credentials=self.creds)
        query: str = f"from:{settings.FORM_BUILDER_EMAIL} label:unread"
        msg_list: List[Dict[str, str]] = service.users().messages().list(
            userId=self.user_id, q=query).execute()['messages']

        m: Dict[str, str]
        for m in msg_list:
            mail: Dict[str, Any] = service.users().messages().get(userId=self.user_id, id=m["id"]).execute()
            mail_body: str = base64.urlsafe_b64decode(
                mail['payload']['parts'][0]['parts'][0]['parts'][0]['body']['data']).decode("ascii")

            payload: Dict[str, Any] = self.build_payload(mail_body)

    @staticmethod
    def _build_address(address: str) -> Dict[str, Any]:
        try:
            address_comp = address.split("\r\n")
            street_lines = address_comp[0].split(",")
            city_comp = address_comp[1].split(" ")

            ret: Dict[str, Any] = {
                "street_line1": street_lines[0],
                "street_line2": street_lines[1] if len(street_lines) > 2 else "",
                "street_line3": street_lines[2] if len(street_lines) > 3 else "",
                "city": city_comp[0],
                "state": city_comp[1],
                "post_code": city_comp[2],
                "country": address_comp[2]
            }
        except Exception as e:
            logger.error(f"Cannot parse address ({address}) ({str(e)}). Falling back to raw_address.")
            ret: Dict[str, Any] = {
                "raw_address": address
            }

        return ret


@app.task()
def check_email():
    # plasma.logs.setup("citygroves", "appgen")
    logger.info("checking email.")
