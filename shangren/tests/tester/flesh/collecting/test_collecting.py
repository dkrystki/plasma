from stickybeak.injector import DjangoInjector
from rhei import Stopwatch
from shang.tests.e2e import Chart
import pytest


@pytest.fixture()
def collector_bitstamp():
    datacolls_bitstamp = Chart(path="../../datacolls/bitstamp", values={
        "sentry": {
            "dsn": "http://4f571e554f224e5ab0a91727da85b5e4@sentry.sentry/2"
        },

        "bitstamp": {
            "url": "ws://bitstamp.mockexchs:8000/ws/",
            "supportedCurrencies": ["btc", "bch", "eth", "ltc", "xrp"]
        }
    })
    datacolls_bitstamp.start()

    mockexchs_bitstamp = Chart(path="../../mockexchs/bitstamp", values={
        "sentry": {
            "dsn": "http://4f571e554f224e5ab0a91727da85b5e4@sentry.sentry/2"
        },
    })
    mockexchs_bitstamp.start()

    init_stopwatch = Stopwatch()
    init_stopwatch.start()
    bitstamp = DjangoInjector(address='http://bitstamp-e2e.mockexchs:8000',
                              django_settings_module='bitstamp.settings')

    @bitstamp.klass
    class MeBitstamp:
        @classmethod
        def produce(cls) -> None:
            from core.management.commands.produce import command
            command.callback("data/recordings/2019-06-23_14:08:43_R5.json")

    init_stopwatch.pause()

    yield MeBitstamp
    datacolls_bitstamp.delete()
    mockexchs_bitstamp.delete()


def test_sample_data(collector_bitstamp):
    collector_bitstamp.produce()
    b = 2
