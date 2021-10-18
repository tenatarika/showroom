from rest_framework import serializers
from .models import Customer, Purchase


class GetCustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = (
            "name",
            "description",
            "width",
            "mileage",
            "price",
            "vin",
        )



    #     name = models.CharField(max_length=50)
    # birthday = models.DateField(blank=True, null=True)
    # phone = models.CharField(max_length=14)
    # balance = DecimalRangeField(null=True, min_value=0, max_value=9999999, decimal_places=2, max_digits=10) 
    # sample = models.JSONField(blank=True, default=jsonfield_default_value)
    # cars = models.ManyToManyField(Car, through='Purchase')
    # country = CountryField(default=None, blank=True)