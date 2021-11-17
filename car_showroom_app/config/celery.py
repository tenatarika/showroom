import os
from celery import Celery
from celery.schedules import crontab
from celery._state import _set_current_app

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('config')
app.config_from_object('django.conf:settings', namespace='CELERY')
_set_current_app(app)
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'buy-car-showroom-every-single-minute': {
        'task': 'src.car_showroom.tasks.showroom_task',
        'schedule': crontab(minute='*/1'),
    },

    'buy-car-customer-every-two-minutes': {
        'task': 'src.customer.tasks.customer_task',
        'schedule': crontab(minute='*/2'),
    },

}
