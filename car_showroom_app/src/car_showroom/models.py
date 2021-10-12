from django.db import models

from src.supplier.models import Car
from django_countries.fields import CountryField
# Create your models here.

class Car_showroom(models.Model):
    
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, max_length=255)
    balance = models.DecimalField(max_digits=14, decimal_places=2)
    car = models.ManyToManyField(Car, through='Car_showroom_Car')
    sortquery = models.JSONField(blank=True, default=None)
    country = CountryField(default=None, blank=True)

    def __str__(self):
        return self.name




class Car_showroom_Car(models.Model):
    """buying a car from a provider
    """

    count = models.IntegerField(default=1)
    discount = models.DecimalField(max_digits =10, decimal_places=2, default=0)
    date = models.DateTimeField(auto_now=True)
    car = models.ForeignKey(Car, to_field='vin', on_delete=models.CASCADE)
    сar_showroom = models.ForeignKey(Car_showroom, on_delete=models.CASCADE)
    

