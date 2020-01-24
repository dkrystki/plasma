import base64
from datetime import datetime
from typing import Dict, Any
import re

import environ

from appgen.celer import app
from django.conf import settings
from googleapiclient.discovery import build, Resource
from google.oauth2.credentials import Credentials

from citygroves.api_clients import backend

from celery.utils.log import get_task_logger

env = environ.Env()

logger = get_task_logger(__name__)


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

    def _build_application(self, mail_body: str) -> backend.Application:
        values = [s.strip() for s in re.split(r"\*.*?\*", mail_body, flags=re.DOTALL) if s]

        def yes_no_to_bool(x: str) -> bool: return {"yes": True, "no": False}[x]

        application = backend.Application(person=backend.Person(first_name=values[0].split()[0],
                                                                last_name=values[0].split()[1],
                                                                email=values[1],
                                                                phone=values[2],
                                                                dob=datetime.strptime(values[3], "%m/%d/%Y").date()),
                                          unit_number=int(values[4]),
                                          room_number=int(values[5]),
                                          current_address=self._build_address(values[6]),
                                          number_of_ppl_to_move_in=int(values[7]),
                                          move_in_date=datetime.strptime(values[8], "%m/%d/%Y").date(),
                                          guarantor_will_pay=yes_no_to_bool(values[13]),
                                          is_employed=yes_no_to_bool(values[14]),
                                          centerlink_will_pay=yes_no_to_bool(values[15]),
                                          have_sufficient_funds=yes_no_to_bool(values[16]),
                                          is_local_student=yes_no_to_bool(values[18]),
                                          is_international_student=yes_no_to_bool(values[19]),
                                          is_young_professional=yes_no_to_bool(values[20]),
                                          referrers=[
                                              backend.Referrer(first_name=values[23].split()[0] if len(
                                                  values[23].split()) > 1 else None,
                                                               last_name=values[23].split()[1] if len(
                                                                   values[23].split()) > 2 else None,
                                                               email=values[25] if values[25] else None,
                                                               phone=values[26] if values[25] else None,
                                                               address=self._build_address(values[27])),
                                              backend.Referrer(first_name=values[29].split()[0] if len(
                                                  values[29].split()) > 1 else None,
                                                               last_name=values[29].split()[1] if len(
                                                                   values[29].split()) > 2 else None,
                                                               email=values[33] if values[33] else None,
                                                               phone=values[32] if values[32] else None,
                                                               address=self._build_address(values[31])
                                                               )])

        return application

    def fetch_all(self) -> None:
        logger.info("Checking email.")

        service: Resource = build('gmail', 'v1', credentials=self.creds)
        query: str = f"from:{settings.FORM_BUILDER_EMAIL} label:unread"
        msg_list: Dict[str, Any] = service.users().messages().list(
            userId=self.user_id, q=query).execute()

        if 'messages' not in msg_list:
            logger.info("Nothing found.")
            return

        logger.info(f"Found {msg_list['resultSizeEstimate']} emails.")

        m: Dict[str, str]
        for m in msg_list['messages']:
            logger.info(f"Fetching email (id={m['id']}).")

            mail: Dict[str, Any] = service.users().messages().get(userId=self.user_id, id=m["id"]).execute()
            service.users().messages().modify(userId=self.user_id,
                                              id=m["id"],
                                              body={'removeLabelIds': ['UNREAD']}).execute()
            logger.info(f"Fetched email (snippet={mail['snippet']}).")

            mail_body: str = base64.urlsafe_b64decode(
                mail['payload']['parts'][0]['parts'][0]['parts'][0]['body']['data']).decode("ascii")

            application: backend.Application = self._build_application(mail_body)
            backend_api = backend.Backend(env.str("BACKEND_API_URL"))

            logger.info(f"Sending application to backend.")
            backend_api.applications.create(application)

    @staticmethod
    def _build_address(address: str) -> backend.Address:
        try:
            address_comp = address.split("\r\n")
            street_lines = address_comp[0].split(",")
            city_comp = address_comp[1].split(" ")

            ret = backend.Address(street_line1=street_lines[0],
                                  street_line2=street_lines[1] if len(street_lines) > 2 else "",
                                  street_line3=street_lines[2] if len(street_lines) > 3 else "",
                                  city=city_comp[0],
                                  state=city_comp[1],
                                  post_code=city_comp[2],
                                  country=address_comp[2],
                                  raw_address=address)
        except Exception as e:
            logger.error(f"Cannot parse address ({address}) ({str(e)}). Falling back to raw_address.")
            ret = backend.Address(raw_address=address)

        return ret


@app.task()
def check_email():
    f = Fetcher()
    f.fetch_all()
