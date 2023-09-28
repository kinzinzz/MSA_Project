from __future__ import absolute_import, unicode_literals
from celery import Celery
import os


rabbitmq_user = os.environ['RABBITMQ_USER']
rabbitmq_password = os.environ['RABBITMQ_PASSWORD']

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'User.settings')

app = Celery('User', broker=f'amqps://{rabbitmq_user}:{rabbitmq_password}@dingo.rmq.cloudamqp.com/{rabbitmq_user}')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()