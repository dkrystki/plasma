from shang.utils.deploy import Namespace

from tests import tester


def deploy() -> None:
    tests = Namespace("tests")
    tests.create()

    tester.deploy()
