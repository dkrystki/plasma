from stickybeak.injector import DjangoInjector

me_bitstamp = DjangoInjector(address='http://bitstamp.mockexchs:8000',
                             django_settings_module='bitstamp.settings')


@me_bitstamp.klass
class MeBitstamp:
    @classmethod
    def test(cls):
        return "a"


def test_sample_data():
    a = MeBitstamp.test()
    b = 2
