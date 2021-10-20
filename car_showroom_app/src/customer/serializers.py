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
