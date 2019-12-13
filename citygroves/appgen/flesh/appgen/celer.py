import os
from django.conf import settings
from celery import Celery
from celery import signals

import plasma.logs
plasma.logs.setup("citygroves", "appgen")

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'appgen.settings')
app = Celery('appgen')

app.conf.update({
    'broker_url': "redis://:password@redis-master:6379",
    'worker_hijack_root_logger': False
})
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

app.conf.timezone = 'UTC'


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    from appgen import tasks
    sender.add_periodic_task(60.0, tasks.check_email.s(), expires=10)


@signals.setup_logging.connect
def setup_celery_logging(**kwargs):
    pass
