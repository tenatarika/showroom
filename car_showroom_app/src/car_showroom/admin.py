from django.contrib import admin

# Register your models here.
from src.car_showroom.models import Car_showroom, Car_showroom_Car

@admin.register(Car_showroom)
class ShowroomAdmin(admin.ModelAdmin):
    list_display = ("name", "balance", "sortquery", "country")

@admin.register(Car_showroom_Car)
class CarSroomCarAdmin(admin.ModelAdmin):
    list_display = ("count", "discount", "date", "car", "сar_showroom")



# class Car_showroom_Car(models.Model):
#     """buying a car from a provider
#     """

#     count = models.IntegerField(default=1)
#     discount = models.IntegerField(
#                           validators=[MinValueValidator(0),
#                                       MaxValueValidator(100)])
#     date = models.DateTimeField(auto_now=True)
#     car = models.ForeignKey(Car, to_field='vin', on_delete=models.CASCADE)
#     сar_showroom = models.ForeignKey(Car_showroom, on_delete=models.CASCADE)
    

