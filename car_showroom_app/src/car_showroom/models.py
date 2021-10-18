from django.db import models

from src.supplier.models import Car
from django_countries.fields import CountryField
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

def jsonfield_default_value() -> list[int]: # This is a callable
    return [0, 0]

class Car_showroom(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, max_length=255)
    balance = models.DecimalField(max_digits=14, decimal_places=2)
    car = models.ManyToManyField(Car, through='Car_showroom_Car')
    sortquery = models.JSONField(blank=True, default=jsonfield_default_value)
    country = CountryField(default=None, blank=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name




class Car_showroom_Car(models.Model):
    """buying a car from a provider
    """

    is_active = models.BooleanField(default=False)
    count = models.IntegerField(default=1)
    discount = models.IntegerField(
                          validators=[MinValueValidator(0),
                                      MaxValueValidator(100)])
    date = models.DateTimeField(auto_now=True)
    car = models.ForeignKey(Car, to_field='vin', on_delete=models.CASCADE)
    сar_showroom = models.ForeignKey(Car_showroom, on_delete=models.CASCADE)
