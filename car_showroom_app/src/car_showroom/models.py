from src.tools.abstract_models import CreatedAt, UpdatedAt, SoftDelete
from src.tools.fields import DecimalRangeField
from django.db import models
from src.supplier.models import Car, Supplier
from django.core.validators import MaxValueValidator, MinValueValidator


def jsonfield_default_value():  # This is a callable
    return [{'name': 'None'}, {'mileage': 0}, {'width': 0}, {'price': 0}]


class CarShowroom(CreatedAt, UpdatedAt, SoftDelete):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    balance = DecimalRangeField(
        null=True,
        min_value=0, max_value=9999999,
        decimal_places=2, max_digits=10
    )
    cars = models.ManyToManyField(Car, through='CarsOfShowroom')
    sortquery = models.JSONField(blank=True, default=jsonfield_default_value)
    location = models.ForeignKey('customer.Location', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class CarsOfShowroom(CreatedAt, UpdatedAt, SoftDelete):
    """buying a car from a provider"""
    count = models.IntegerField(default=1)
    discount = models.IntegerField(
                          validators=[MinValueValidator(1),
                                      MaxValueValidator(100)])
    car = models.ForeignKey(Car, to_field='vin', on_delete=models.SET_NULL,
                            related_name='cars_of_showroom', related_query_name='car_of_showroom',
                            null=True)
    сar_showroom = models.ForeignKey(CarShowroom, on_delete=models.CASCADE,
                                     related_name='showrooms', related_query_name='showroom',
                                     null=True, blank=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE,
                                 related_name='suppliers', related_query_name='supplier',
                                 null=True, blank=True)

