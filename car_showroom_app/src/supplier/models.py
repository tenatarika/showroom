from django.core.validators import RegexValidator, MaxValueValidator, MinValueValidator
from django.db import models

from src.core.enums.supplier import Color
from src.tools.abstract_models import CreatedAt, UpdatedAt, SoftDelete
from src.tools.fields import DecimalRangeField


class Car(CreatedAt, UpdatedAt, SoftDelete):
    """Car model"""

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, max_length=255)
    width = models.IntegerField(blank=True, validators=(MinValueValidator(1),))
    mileage = models.IntegerField(blank=True, null=True, validators=(MinValueValidator(0),))
    price = DecimalRangeField(
        null=True,
        min_value=0, max_value=9999999,
        decimal_places=2, max_digits=10
    )
    year = models.PositiveIntegerField(blank=True, default='1900',
                                       validators=(MaxValueValidator(2021),))
    color = models.CharField(max_length=7, default='white', blank=True, choices=Color.choices())

    vin = models.CharField(
        max_length=17,
        unique=True,
        validators=(
            RegexValidator(regex="^[A-HJ-NPR-Za-hj-npr-z\d]{8}[\dX][A-HJ-NPR-Za-hj-npr-z\d]{2}\d{6}$"),
        )
    )

    def __str__(self):
        return self.name


class Supplier(CreatedAt, UpdatedAt, SoftDelete):
    """provider"""

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, max_length=255)
    balance = DecimalRangeField(
        null=True,
        min_value=0, max_value=9999999,
        decimal_places=2, max_digits=10
    )
    cars = models.ManyToManyField(Car, through='SupplierCar')

    def __str__(self):
        return self.name


class SupplierCar(CreatedAt, UpdatedAt, SoftDelete):
    """Buying cars"""

    count = models.PositiveIntegerField(default=1)
    discount = DecimalRangeField(
        max_digits=10,
        decimal_places=2,
        default=1,
        min_value=1,
        max_value=100,
    )
    car = models.ForeignKey(Car, to_field='vin', on_delete=models.SET_NULL,
                            related_name='suppliers', related_query_name='supplier',
                            null=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE,
                                 related_name='supplier_cars', related_query_name='supplier_car',
                                 null=True)


class SupplierSale(CreatedAt, UpdatedAt, SoftDelete):
    """Supplier sale"""
    car = models.ForeignKey(Car, to_field='vin', on_delete=models.SET_NULL,
                            related_name='cars_sale', related_query_name='car_sale',
                            null=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE,
                                 related_name='supplier_sale', related_query_name='supplier_sale',
                                 null=True)
    discount = DecimalRangeField(
        max_digits=10,
        decimal_places=2,
        default=1,
        min_value=1,
        max_value=100,
    )
    end_date = models.DateField(blank=True)
