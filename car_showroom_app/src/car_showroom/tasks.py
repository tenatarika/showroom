from config.celery import app
from src.car_showroom.services import buy_cars


@app.task
def showroom_task():
    buy_cars.delay()
