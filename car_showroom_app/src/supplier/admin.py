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
    list_display = ('name', 'balance')


@admin.register(SupplierCar)
class CarsOfSupplierAdmin(admin.ModelAdmin):
    list_display = ('count', 'discount', 'date', 'car', 'supplier')
