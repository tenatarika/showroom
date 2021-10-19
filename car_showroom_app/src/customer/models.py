from django.db import models
from django_countries.fields import CountryField
from src.supplier.models import Car
from src.car_showroom.models import CarShowroom
from src.car_showroom.models import jsonfield_default_value
from src.tools.fields import DecimalRangeField
from django.core.validators import MaxValueValidator, MinValueValidator



class Customer(models.Model):
    name = models.CharField(max_length=50)
    birthday = models.DateField(blank=True, null=True)
    phone = models.CharField(max_length=14)
    balance = DecimalRangeField(
        null=True,
        min_value=0, max_value=9999999,
        decimal_places=2, max_digits=10
        )
    sample = models.JSONField(blank=True, default=jsonfield_default_value)
    cars = models.ManyToManyField(Car, through='Purchase')
    country = CountryField(default=None, blank=True)

    def __str__(self):
        return self.name


class Purchase(models.Model):
    car = models.ForeignKey(Car, to_field='vin', on_delete=models.CASCADE)
    supplier = models.ForeignKey(Customer, on_delete=models.CASCADE)
    car_showroom = models.ForeignKey(CarShowroom, on_delete=models.CASCADE)
    discount = models.IntegerField(
                          validators=[MinValueValidator(0),
                                      MaxValueValidator(100)])
