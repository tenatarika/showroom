from django.db.models import Q, F
from src.car_showroom.models import CarsOfShowroom, ShowroomSale
from src.customer.models import Customer, Purchase
from config.celery import app


@app.task
def customer_buy_car():
    """Functions for buy cars customers"""
    for customer in Customer.objects.all():
        sample = customer.sample

        find_showroom_q = (Q(car__name__startswith=sample[0].get('name')) &
                           Q(car__mileage__lte=sample[1].get('mileage')) &
                           Q(car__width__gte=sample[2].get('width')) &
                           Q(car__price__lte=sample[3].get('price')))

        showroom_discounts = CarsOfShowroom.objects.filter(find_showroom_q).order_by('-discount').first()
        sale_discount = ShowroomSale.objects.filter(find_showroom_q).order_by('-discount').first()

        if showroom_discounts is None and sale_discount is None:
            continue
        elif sale_discount is None:
            customer_purchase = showroom_discounts
        elif showroom_discounts is None:
            customer_purchase = sale_discount
        elif showroom_discounts.discount > sale_discount.discount:
            customer_purchase = showroom_discounts
        else:
            customer_purchase = sale_discount

        if customer.balance >= customer_purchase.car.price:
            customer.balance -= customer_purchase.car.price
            customer_purchase.car_showroom.balance += customer_purchase.car.price

            purchase = Purchase.objects.filter(car=customer_purchase.car, car_showroom=customer_purchase.car_showroom,
                                               customer=customer).first()

            if purchase is not None:
                Purchase.objects.filter(car=customer_purchase.car, car_showroom=customer_purchase.car_showroom,
                                        customer=customer).update(count=F('count') + 1)

                customer.save()
                customer_purchase.car_showroom.save()
            else:
                pur = Purchase.objects.create(discount=customer_purchase.discount, car=customer_purchase.car,
                                              car_showroom=customer_purchase.car_showroom, customer=customer)

                pur.save()
                customer.save()
                customer_purchase.car_showroom.save()
