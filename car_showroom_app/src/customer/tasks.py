from config.celery import app
from src.customer.services import customer_buy_car


@app.task
def customer_task():
    customer_buy_car.delay()
