import os

from ..devops import run


def test_run():
    run("echo test")
    os.system("echo test123")
    print("fdsfd")
    os.system("echo test && sleep 5 && echo haha")
    print("xcvvvvcx")
    os.system("echo aha")
