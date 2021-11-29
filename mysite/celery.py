import os
from celery import Celery

# setting default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

app = Celery('mysite')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()