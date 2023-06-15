import os
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mcdonalds.settings')

app = Celery('NewsPapper')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'send_mail_every_week': {
        'task': 'basis.tasks.send_mail',
        'schedule': crontab(hour=8, minute=00, day_of_week='monday')
    },

    'send_mail_add_news': {
        'task': 'basis.tasks.send_notifications',
        'schedule': crontab(),
    }
}