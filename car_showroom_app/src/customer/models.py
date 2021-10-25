from django.db import models
from django_countries.fields import CountryField
from src.supplier.models import Car
from src.car_showroom.models import CarShowroom
from src.car_showroom.models import jsonfield_default_value
from src.tools.fields import DecimalRangeField
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator

class Customer(models.Model):
    name = models.CharField(max_length=50)
    birthday = models.DateField(blank=True, null=True)
    phone = models.CharField(
        max_length=14,
        validators=[
        RegexValidator(regex="^\+375 \((17|29|33|44)\) [0-9]{3}-[0-9]{2}-[0-9]{2}$")
    ])


    balance = DecimalRangeField(
        null=True,
        min_value=0, max_value=9999999,
        decimal_places=2, max_digits=10
        )
    sample = models.JSONField(blank=True, default=jsonfield_default_value)
    cars = models.ManyToManyField(Car, through='Purchase')
    country = CountryField(default=None, blank=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("name", "balance", "country")


class Purchase(models.Model):
    is_active = models.BooleanField(default=False)
    car = models.ForeignKey(Car, to_field='vin', on_delete=models.CASCADE)
    supplier = models.ForeignKey(Customer, on_delete=models.CASCADE)
    showroom = models.ForeignKey(CarShowroom, on_delete=models.CASCADE, blank=True)
    discount = models.IntegerField(
                          validators=[MinValueValidator(0),
                                      MaxValueValidator(100)])
