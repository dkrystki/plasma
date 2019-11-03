import sentry_sdk
import environ

env = environ.Env()


class Bitstamp:
    SUPPORTED_CURRENCIES = env.list("SUPPORTED_CURRENCIES")
    URL = env.str("BITSTAMP_URL")


class Sentry:
    DSN = env.str("SENTRY_DSN")


sentry_sdk.init(Sentry.DSN)


a = 11611824

