from rest_framework import serializers
from .models import Car_showroom, Car_showroom_Car


class GetPublicShowroom(serializers.ModelSerializer):

    class Meta:
        model = Car_showroom

        fields = ('name', 'description', 'country')


class GetCarsOfShowroom(serializers.ModelSerializer):

    class Meta:
        model = Car_showroom_Car
        fields = ('count', 'discount', 'date', 'car') 
