from rest_framework import serializers
from .models import Customer, Purchase


class GetCustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = (
            "name",
            "birthday",
            "country",
            "phone",
        )


class GetPrivateCustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = (
            "name",
            "balance",
            "phone",
            "sample",
            "country",
            "is_active",
        )


class GetPurchaseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Purchase
        fields = (
            'car',
            'supplier',
            'car_showroom',
            'discount',
        )
