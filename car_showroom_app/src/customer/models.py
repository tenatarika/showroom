from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator
from django.db import models
from django_countries.fields import CountryField

from src.car_showroom.models import CarShowroom
from src.car_showroom.models import jsonfield_default_value
from src.core.customer.gender import Gender
from src.supplier.models import Car
from src.tools.fields import CreatedAt, UpdatedAt, SoftDelete
from src.tools.fields import DecimalRangeField


class Location(CreatedAt, UpdatedAt, SoftDelete):
    country = CountryField(default=None, blank=True, null=True)
    city = models.CharField(default=None, max_length=200, blank=True, null=True)
    street = models.CharField(default=None, max_length=200, blank=True, null=True)
    houseNum = models.PositiveIntegerField(default=None, blank=True, null=True)

    def __str__(self):
        return f'{self.country}, {self.city}, {self.street}, {self.houseNum}'


class Customer(CreatedAt, UpdatedAt, SoftDelete):
    name = models.CharField(max_length=50)
    gender = models.CharField(choices=Gender.choices(), default="MALE", max_length=50)
    birthday = models.DateField(blank=True, null=True)
    phone = models.CharField(
        max_length=40,
        validators=(
            RegexValidator(regex="^\+375(17|29|33|44)[0-9]{3}[0-9]{2}[0-9]{2}$"),
        )
    )

    balance = DecimalRangeField(
        null=True,
        min_value=0, max_value=9999999,
        decimal_places=2, max_digits=10
    )
    sample = models.JSONField(blank=True, default=jsonfield_default_value)
    cars = models.ManyToManyField(Car, through='Purchase')
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("name", "balance",)


class Purchase(CreatedAt, UpdatedAt, SoftDelete):
    car = models.ForeignKey(Car, to_field='vin', on_delete=models.SET_NULL,
                            related_name='cars', related_query_name='car',
                            null=True, blank=True)
    supplier = models.ForeignKey(Customer, on_delete=models.SET_NULL,
                                 related_name='suppliers', related_query_name='supplier',
                                 null=True, blank=True)
    car_showroom = models.ForeignKey(CarShowroom, on_delete=models.SET_NULL,
                                     related_name='carShowrooms', related_query_name='carShowroom',
                                     null=True, blank=True)
    discount = models.IntegerField(
        validators=(MinValueValidator(0),
                    MaxValueValidator(100),))

