from celery import shared_task
from .models import Task
import logging
from django.utils.timezone import now
from datetime import timedelta

logger = logging.getLogger(__name__)

@shared_task
def check_old_tasks():
    one_week_ago = now() - timedelta(days=7)
    old_tasks = Task.objects.filter(completed=False, created_at__lt=one_week_ago)

    for task in old_tasks:
        logger.warning(f'Task "{task.title}" is incomplete for more than 7 days!')