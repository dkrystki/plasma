from typing import Dict, Any

from google_auth_oauthlib.flow import InstalledAppFlow

from appgen.celer import app
from loguru import logger
from django.conf import settings


class Fetcher:
    def __init__(self):
        from google_auth_oauthlib.flow import Flow
        from googleapiclient.discovery import build
        from google.oauth2.credentials import Credentials

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

        creds: Credentials = Credentials(
            None,
            refresh_token='1//0g_HVOsbpO8C8CgYIARAAGBASNwF-L9Ir2eMZbyB9gZBQFcJIwgUQ6JxqCoAiSUQqf-4sHFg2xnTN7-p0rXDQ_-o8QC_IVZ02gqA',
            token_uri=settings.GMAIL.GOOGLE_TOKEN_URI,
            client_id=settings.GMAIL.CLIENT_ID,
            client_secret=settings.GMAIL.CLIENT_SECRET,

        )

        service = build('gmail', 'v1', credentials=creds)
        result = service.users().messages().list(userId="plasmakwazar.test@gmail.com",
                                        q="from:damian.krystkiewicz@gmail.com").execute()

        mail = service.users().messages().get(userId="plasmakwazar.test@gmail.com",
                                              id=result["messages"][0]["id"]).execute()

        base64.urlsafe_b64decode(mail['payload']['parts'][0]['parts'][0]['parts'][0]['body']['data']).decode("ascii")
        a = 1

@app.task()
def check_email():
    # plasma.logs.setup("citygroves", "appgen")
    logger.info("checking email.")


f = Fetcher()
