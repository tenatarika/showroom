from rest_framework import serializers

from .models import Car, Supplier, Supplier_Car


class GetCarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car
        exclude = (
            "name",
            "description",
            "width",
            "mileage",
            "price",
            "vin"
        )



class GetPublicSupplierSerializer(serializers.ModelSerializer):

    class Meta:
        model = Supplier
        exclude = (
            "name",
            "description",
        )


class GetPrivateSupplierSerializer(serializers.ModelSerializer):

    class Meta:
        model = Supplier
        exclude = (
            "name",
            "description",
            "balance",

        )

    #     name = models.CharField(max_length=100)
    # description = models.TextField(blank=True, max_length=255)
    # balance = models.DecimalField(max_digits=14, decimal_places=2)
    # car = models.ManyToManyField(Car, through='Supplier_Car')
