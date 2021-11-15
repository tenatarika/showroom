from django.db.models import Q, F

from src.car_showroom.models import CarShowroom, CarsOfShowroom
from src.supplier.models import SupplierCar, SupplierSale
from config.celery import app


@app.task
def buy_cars():
    """Function for buying cars"""
    for showroom in CarShowroom.objects.all():
        sample = showroom.sortquery

        find_suppliers_q = (Q(car__name__startswith=sample[0].get('name')) &
                            Q(car__mileage__lte=sample[1].get('mileage')) &
                            Q(car__width__gte=sample[2].get('width')) &
                            Q(car__price__lte=sample[3].get('price')))

        suppliers_discounts = SupplierCar.objects.filter(find_suppliers_q).order_by('-discount').first()
        sale_discount = SupplierSale.objects.filter(find_suppliers_q).order_by('-discount').first()

        if suppliers_discounts is None and sale_discount is None:
            continue
        elif sale_discount is None:
            supplier_purchase = suppliers_discounts
        elif suppliers_discounts is None:
            supplier_purchase = sale_discount
        elif suppliers_discounts.discount > sale_discount.discount:
            supplier_purchase = suppliers_discounts
        else:
            supplier_purchase = sale_discount

        if showroom.balance >= supplier_purchase.car.price:
            showroom.balance -= supplier_purchase.car.price
            supplier_purchase.supplier.balance += supplier_purchase.car.price

            purchase = CarsOfShowroom.objects.filter(car=supplier_purchase.car, сar_showroom=showroom,
                                                     supplier=supplier_purchase.supplier).first()

            if purchase is not None:
                CarsOfShowroom.objects.filter(car=supplier_purchase.car, сar_showroom=showroom,
                                              supplier=supplier_purchase.supplier).update(count=F('count') + 1)

                showroom.save()
                supplier_purchase.supplier.save()
            else:
                pur = CarsOfShowroom.objects.create(discount=supplier_purchase.discount, car=supplier_purchase.car,
                                                    сar_showroom=showroom, supplier=supplier_purchase.supplier)

                pur.save()
                showroom.save()
                supplier_purchase.supplier.save()
