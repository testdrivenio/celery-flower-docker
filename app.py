import os

from celery import Celery


os.environ.setdefault('CELERY_CONFIG_MODULE', 'celery_config')

app = Celery('app')
app.config_from_envvar('CELERY_CONFIG_MODULE')


@app.task
def add(x, y):
    return x + y
