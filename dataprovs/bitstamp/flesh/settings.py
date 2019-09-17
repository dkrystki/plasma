import sentry_sdk
from environs import Env

env = Env()


class Bitstamp:
    SUPPORTED_CURRENCIES = ['btc', 'bch', 'eth', 'ltc', 'xrp']
    URL = env("BITSTAMP_URL")


class Sentry:
    DSN = env("SENTRY_DSN")


sentry_sdk.init(Sentry.DSN)
