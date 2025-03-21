import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todo.settings')

app = Celery('todo')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'check-old-tasks-every-minute': {
        'task': 'tasks.tasks.check_old_tasks',
        'schedule': crontab(minute='*/1'),
    },
}