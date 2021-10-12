from django.db import models

# Create your models here.

class Car(models.Model):
    """Car model
    """


    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, max_length=255)
    width = models.IntegerField(blank=True)
    mileage = models.IntegerField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    vin = models.CharField(max_length=17, unique=True)

    def __str__(self):
        return self.name



class Supplier(models.Model):
    """provider
    """

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, max_length=255)
    balance = models.DecimalField(max_digits=14, decimal_places=2)
    car = models.ManyToManyField(Car, through='Supplier_Car')

    def __str__(self):
        return self.name


class Supplier_Car(models.Model):
    """Buying cars
    """
    count = models.IntegerField(default=1)
    discount = models.DecimalField(max_digits =10, decimal_places=2, default=0)
    date = models.DateTimeField(auto_now=True)
    car = models.ForeignKey(Car, to_field='vin', on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
