import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pinboard.settings')

app = Celery('pinboard')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()