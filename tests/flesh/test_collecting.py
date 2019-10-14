from stickybeak.injector import DjangoInjector
from rhei import Stopwatch

init_stopwatch = Stopwatch()
init_stopwatch.start()
me_bitstamp = DjangoInjector(address='http://bitstamp.mockexchs:8000',
                             django_settings_module='bitstamp.settings')
init_stopwatch.pause()


@me_bitstamp.klass
class MeBitstamp:
    @classmethod
    def produce(cls) -> None:
        from core.management.commands.produce import command
        command.callback("data/recordings/2019-06-23_14:08:43_R5.json")


def test_sample_data():
    MeBitstamp.produce()
    b = 2
