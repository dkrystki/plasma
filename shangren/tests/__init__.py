def deploy() -> None:
    from shang.utils.deploy import Namespace
    from tests import tester

    tests = Namespace("tests")
    tests.create()

    tester.deploy()
