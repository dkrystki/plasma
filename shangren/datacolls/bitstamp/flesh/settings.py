import sentry_sdk
import environ
import shang.logs

env = environ.Env()
shang.logs.setup("datacolls.bitstamp")


class Bitstamp:
    SUPPORTED_CURRENCIES = env.list("SUPPORTED_CURRENCIES")
    URL = env.str("BITSTAMP_URL")


class SENTRY:
    DSN = env.str("SENTRY_DSN")


sentry_sdk.init(SENTRY.DSN)
