from os import environ as env
from celery import Celery

celery = Celery(
    'vackup',
    broker=env.get('CELERY_BROKER_URL', 'redis://redis:6379'),
    backend=env.get('CELERY_RESULT_BACKEND', 'redis://redis:6379')
)
