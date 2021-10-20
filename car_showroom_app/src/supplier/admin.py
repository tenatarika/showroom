from typing import Counter
from django.contrib import admin
from src.supplier.models import Car, Supplier, SupplierCar
from django.urls import reverse
from django.utils.http import  urlencode

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('name', 'width', 'mileage', 'price', 'vin')


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'balance', 'show_cars')

    def show_cars(self, obj):
        result = SupplierCar.objects.all().values('count').last()
        return result.get('count')
    show_cars.short_description = "Amount cars"


@admin.register(SupplierCar)
class CarsOfSupplierAdmin(admin.ModelAdmin):
    list_display = ('count', 'discount', 'date', 'car', 'supplier')
