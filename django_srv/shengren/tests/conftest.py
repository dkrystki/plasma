import pytest
from shengren.systests import Injector


@pytest.fixture(scope="class")
def flask_injector(request):
    request.cls.injector = Injector(address=f'http://flask_srv:5000')


@pytest.fixture(scope="class")
def django_injector(request):
    request.cls.injector = Injector(address=f'http://django_srv:5000')
