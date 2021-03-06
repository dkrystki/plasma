import base64
import logging
from email.mime.multipart import MIMEMultipart
from typing import Optional

from google.oauth2.credentials import Credentials
from googleapiclient import _auth
from googleapiclient.discovery import Resource, build

logger = logging.getLogger(__name__)


class Gmail:
    def __init__(self, refresh_token: str, token_uri: str, client_id: str, client_secret: str, owner_email: str):
        self.creds: Credentials = Credentials(
            None, refresh_token=refresh_token, token_uri=token_uri, client_id=client_id, client_secret=client_secret
        )
        self.user_id: str = owner_email
        self.service: Optional[Resource] = None
        self.http = _auth.authorized_http(self.creds)

    def _connect(self):
        self.service: Resource = build("gmail", "v1", credentials=self.creds)

    def send_message(self, message: MIMEMultipart):
        if not self.service:
            self._connect()

        raw = base64.urlsafe_b64encode(message.as_bytes())
        raw = raw.decode()
        body = {"raw": raw}

        logger.info(f"Sending email to {message['to']}")
        self.service.users().messages().send(userId=self.user_id, body=body).execute(http=self.http)
