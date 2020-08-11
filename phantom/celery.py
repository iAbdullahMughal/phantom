from __future__ import absolute_import
import os
from celery import Celery, shared_task

from app.core.tasks.task import fine_social_user

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'phantom.settings')
app = Celery('phantom')

app.config_from_object('django.conf.settings', namespace='CELERY')
app.autodiscover_tasks()


@shared_task(name="phantom_ig")
def start_execution(user_name):
    fine_social_user(user_name)

    return {"status": True}

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))