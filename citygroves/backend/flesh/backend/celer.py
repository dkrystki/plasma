import os

from celery import Celery, signals
from django.conf import settings

# set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
app = Celery("backend")

app.conf.update({"broker_url": "redis://:password@redis-master:6379/1", "worker_hijack_root_logger": False})
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

app.conf.timezone = "UTC"


@signals.setup_logging.connect
def setup_celery_logging(**kwargs):
    pass
