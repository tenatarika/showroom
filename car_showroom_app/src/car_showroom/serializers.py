from rest_framework import serializers
from .models import Car_showroom, Car_showroom_Car


class GetPublicShowroom(serializers.ModelSerializer):

    class Meta:
        model = Car_showroom

        fields = ('name', 'description', 'country')


class GetCarsOfShowroom(serializers.ModelSerializer):

    class Meta:
        model = Car_showroom_Car
        fields = ('count', 'discount', 'date', 'car', ) 



    # count = models.IntegerField(default=1)
    # discount = models.IntegerField(
    #                       validators=[MinValueValidator(0),
    #                                   MaxValueValidator(100)])
    # date = models.DateTimeField(auto_now=True)
    # car = models.ForeignKey(Car, to_field='vin', on_delete=models.CASCADE)
    # сar_showroom = models.ForeignKey(Car_showroom, on_delete=models.CASCADE)
    