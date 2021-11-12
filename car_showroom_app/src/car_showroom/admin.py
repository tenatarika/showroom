from django.contrib import admin

# Register your models here.
from src.car_showroom.models import CarShowroom, CarsOfShowroom


@admin.register(CarShowroom)
class ShowroomAdmin(admin.ModelAdmin):
    list_display = ("name", "balance", "sortquery", "location",)


@admin.register(CarsOfShowroom)
class CarsOfShowroomAdmin(admin.ModelAdmin):
    list_display = ('supplier', "count", "discount", "added_date", "car")
