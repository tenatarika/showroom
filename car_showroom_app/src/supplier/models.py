from django.db import models
from django.core.validators import RegexValidator

from src.tools.fields import CreatedAt, UpdatedAt, SoftDelete


class Car(CreatedAt, UpdatedAt, SoftDelete):
    """Car model"""

    class Color(models.TextChoices):
        RED = "Red"
        ORANGE = "Orange"
        YELLOW = "Yellow"
        GREEN = "Green"
        BLUE = "Blue"
        PURPLE = "Purple"
        PINK = "Pink"
        BLACK = "Black"
        WHITE = "White"
        GRAY = "Gray"

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, max_length=255)
    width = models.IntegerField(blank=True)
    mileage = models.IntegerField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    year = models.PositiveIntegerField(blank=True, default='1900')
    color = models.CharField(max_length=200, default='white', blank=True, choices=Color.choices)

    vin = models.CharField(
        max_length=17,
        unique=True,
        validators=(
            RegexValidator(regex="^[A-HJ-NPR-Za-hj-npr-z\d]{8}[\dX][A-HJ-NPR-Za-hj-npr-z\d]{2}\d{6}$"),
        ))

    def __str__(self):
        return self.name


class Supplier(CreatedAt, UpdatedAt, SoftDelete):
    """provider"""

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, max_length=255)
    balance = models.DecimalField(max_digits=14, decimal_places=2)
    cars = models.ManyToManyField(Car, through='SupplierCar')

    def __str__(self):
        return self.name


class SupplierCar(CreatedAt, UpdatedAt, SoftDelete):
    """Buying cars"""

    count = models.IntegerField(default=1)
    discount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=1)
    date = models.DateTimeField(auto_now=True)
    car = models.ForeignKey(Car, to_field='vin', on_delete=models.SET_NULL,
                            related_name='suppliers', related_query_name='supplier',
                            null=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL,
                                 related_name='supplier_cars', related_query_name='supplier_car',
                                 null=True)
