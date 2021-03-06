from rest_framework import serializers

from src.supplier.models import SupplierCar, Car, Supplier


class SupplierPurchasesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupplierCar
        fields = '__all__'


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
            "year",
            "color",
        )


class ListCarSerializer(serializers.ModelSerializer):
    """ list of cars"""
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
            "year",
            "color",
        )


class GetPublicSupplierSerializer(serializers.ModelSerializer):

    class Meta:
        model = Supplier
        fields = ("id", "name", "description",)


class GetSupplierSerializer(serializers.ModelSerializer):

    class Meta:
        model = Supplier
        fields = (
            "name",
            "description",
            "balance",
            "cars",
        )
