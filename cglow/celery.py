import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cglow.settings')

app = Celery('cglow')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()