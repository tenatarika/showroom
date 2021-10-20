from rest_framework import serializers
from .models import Car, Supplier


class GetCarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car
        fields = (
            "name",
            "description",
            "width",
            "mileage",
            "price",
            "vin",
        )


class ListCarSerializer(serializers.ModelSerializer):
    """ list of posts"""
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Car
        fields = (
            "name",
            "description",
            "width",
            "mileage",
            "price",
            "vin",
        )


class GetPublicSupplierSerializer(serializers.ModelSerializer):

    class Meta:
        model = Supplier
        fields = ("id", "name", "description")


class GetSupplierSerializer(serializers.ModelSerializer):

    class Meta:
        model = Supplier
        fields = (
            "name",
            "description",
            "balance",
            "car",
        )
