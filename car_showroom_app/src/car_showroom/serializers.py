from rest_framework import serializers

from src.car_showroom.models import CarShowroom, CarsOfShowroom


class GetPublicShowroom(serializers.ModelSerializer):

    class Meta:
        model = CarShowroom
        fields = ('name', 'description', 'country',)


class GetCarsOfShowroom(serializers.ModelSerializer):

    class Meta:
        model = CarsOfShowroom
        fields = ('count', 'discount', 'date', 'car',)
