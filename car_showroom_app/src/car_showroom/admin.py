from django.contrib import admin

# Register your models here.
from src.car_showroom.models import CarShowroom, CarsOfShowroom


@admin.register(CarShowroom)
class ShowroomAdmin(admin.ModelAdmin):
    list_display = ("name", "balance", "sortquery", "country")


@admin.register(CarsOfShowroom)
class CarsOfShowroomAdmin(admin.ModelAdmin):
    list_display = ("count", "discount", "date", "car")
