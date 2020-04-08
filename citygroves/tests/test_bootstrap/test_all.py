from environ import Env
environ = Env()


def test_all(container):
    c = container
    c.run(["""eval "$(./shell.py --dry-run)" """,
           "bootstrap",
           "cd citygroves",
           'eval "$(./shell.py --dry-run)"',
           "./cluster.py bootstrap_local_dev"])
