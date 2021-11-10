from src.car_showroom.models import CarShowroom, CarsOfShowroom
from src.supplier.models import SupplierCar
from config.celery import app


@app.task
def buy_cars() -> bool:

    for showroom in CarShowroom.objects.all():
        sample = showroom.sortquery
        suppliers = SupplierCar.objects.filter(car__name=sample[0].get('name'))
        for supplier in suppliers:
            if showroom.balance >= suppliers[0].car.price:
                # print(showroom.balance, suppliers[0].supplier.balance)
                showroom.balance -= suppliers[0].car.price
                suppliers[0].supplier.balance += suppliers[0].car.price
                pur = CarsOfShowroom.objects.create(discount=1, car=supplier.car, сar_showroom=showroom)
                # print(showroom.balance, suppliers[0].supplier.balance)
                pur.save()
                showroom.save()
                suppliers[0].supplier.save()
                return True
