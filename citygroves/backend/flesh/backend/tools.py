import base64
from email.mime.multipart import MIMEMultipart
from typing import Optional

from googleapiclient.discovery import build, Resource
from googleapiclient import _auth
from google.oauth2.credentials import Credentials


class Gmail:
    def __init__(self, refresh_token: str, token_uri: str, client_id: str, client_secret: str, owner_email: str):
        self.creds: Credentials = Credentials(
            None,
            refresh_token=refresh_token,
            token_uri=token_uri,
            client_id=client_id,
            client_secret=client_secret,
        )
        self.user_id: str = owner_email
        self.service: Optional[Resource] = None
        self.http = _auth.authorized_http(self.creds)

    def _connect(self):
        self.service: Resource = build('gmail', 'v1', credentials=self.creds)

    def send_message(self, message: MIMEMultipart):
        if not self.service:
            self._connect()

        raw = base64.urlsafe_b64encode(message.as_bytes())
        raw = raw.decode()
        body = {'raw': raw}

        self.service.users().messages().send(userId=self.user_id, body=body).execute(http=self.http)
