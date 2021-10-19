
from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from django.conf import settings
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celery_project.settings')

app = Celery('celery_project')
app.conf.enable_utc = False

app.conf.update(timezone = 'Asia/Kolkata')

app.config_from_object(settings, namespace='CELERY')

# Celery Beat Settings
# app.conf.beat_schedule = {
#     'send-mail-every-2-min': {
#         'task': 'sending_mail.task.send_mail_func',
#         'schedule': crontab(hour=14, minute=54),
#         #'args': (2,)
#     }
    
# }
app.conf.beat_schedule = {
    'add-every-60-seconds': {
        'task': 'sending_mail.task.send_mail_func',
        'schedule': crontab(minute='*/1'),
        
    }
}
app.conf.timezone = 'UTC'

# Celery Schedules - https://docs.celeryproject.org/en/stable/reference/celery.schedules.html

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
