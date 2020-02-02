from django.conf import settings

from backend.tools import Gmail

gmail = Gmail(
    refresh_token=settings.GMAIL.REFRESH_TOKEN,
    token_uri=settings.GMAIL.GOOGLE_TOKEN_URI,
    client_id=settings.GMAIL.CLIENT_ID,
    client_secret=settings.GMAIL.CLIENT_SECRET,
    owner_email=settings.GMAIL.OWNER_EMAIL,
)
