from rest_framework import serializers

from src.customer.models import Customer, Purchase


class GetCustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = (
            "name",
            "birthday",
            "location",
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
            "location",
        )


class GetPurchaseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Purchase
        fields = (
            'car',
            'car_showroom',
            'discount',
        )
