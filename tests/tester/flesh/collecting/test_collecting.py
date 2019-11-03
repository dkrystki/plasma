from stickybeak.injector import DjangoInjector
from rhei import Stopwatch
from shangren.tests.e2e import Chart
import pytest


@pytest.fixture()
def collector_bitstamp():
    chart = Chart(path="../../datacolls/bitstamp", values={
        
    })

    chart.start()

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
    chart.delete()


def test_sample_data(collector_bitstamp):
    collector_bitstamp.produce()
    b = 2
