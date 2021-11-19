from django.contrib import admin

# Register your models here.
from src.car_showroom.models import CarShowroom, CarsOfShowroom, ShowroomSale


@admin.register(ShowroomSale)
class SaleShowroomAdmin(admin.ModelAdmin):
    list_display = ('car', 'car_showroom', 'discount', 'added_date', 'end_date')


@admin.register(CarShowroom)
class ShowroomAdmin(admin.ModelAdmin):
    list_display = ("name", "balance", "sortquery", "location",)


@admin.register(CarsOfShowroom)
class CarsOfShowroomAdmin(admin.ModelAdmin):
    list_display = ('supplier', "count", "discount", "added_date", "date_updated", "car")
