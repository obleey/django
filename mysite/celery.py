import os
from celery import Celery
from celery.schedules import crontab


# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

app = Celery('mysite')
app.conf.enable_utc=False
app.conf.update(timezone='Europe/Belgrade')


app.config_from_object('django.conf:settings', namespace='CELERY')


app.conf.beat_schedule = {
    'send-email-every-day': {
        'task': 'workevidence.tasks.send_email_task',
        'schedule': crontab(hour=22, minute=13),
    },
}

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')