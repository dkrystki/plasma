from shangren.utils.deploy import run


def get_pod_name() -> str:
    return run('kubectl -n sentry get pods -l role=web -o name | grep -m 1 -o "sentry-web.*$"')
