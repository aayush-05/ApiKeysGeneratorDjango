import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'random_keys_generator.settings')
app = Celery('random_keys_generator')
app.config_from_object('django.conf:settings')

app.autodiscover_tasks()
app.conf.beat_schedule = {
    'check_active_status_every_minute': {
        'task': 'keys_api.tasks.check_last_alive',
        'schedule': crontab(),
    },
}
