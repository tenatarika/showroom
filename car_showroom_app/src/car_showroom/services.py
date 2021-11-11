from django.db.models import Q

from src.car_showroom.models import CarShowroom, CarsOfShowroom
from src.supplier.models import SupplierCar
from config.celery import app


@app.task
def buy_cars() -> bool:
    """Function for buying cars"""
    for showroom in CarShowroom.objects.all():
        sample = showroom.sortquery

        find_suppliers_q = (Q(car__name__startswith=sample[0].get('name')) &
                            Q(car__mileage__lte=sample[1].get('mileage')) &
                            Q(car__width__gte=sample[2].get('width')) &
                            Q(car__price__lte=sample[3].get('price')))

        suppliers = SupplierCar.objects.filter(find_suppliers_q)
        for supplier_purchase in suppliers:
            if showroom.balance >= supplier_purchase.car.price:
                showroom.balance -= supplier_purchase.car.price
                supplier_purchase.supplier.balance += supplier_purchase.car.price

                purchase = CarsOfShowroom.objects.filter(car=supplier_purchase.car, сar_showroom=showroom)[0]

                if purchase is not None:
                    purchase.count += 1
                    purchase.save()
                    showroom.save()
                    supplier_purchase.supplier.save()
                else:
                    pur = CarsOfShowroom.objects.create(discount=1, car=supplier_purchase.car, сar_showroom=showroom)
                    pur.save()
                    showroom.save()
                    supplier_purchase.supplier.save()
                return True
