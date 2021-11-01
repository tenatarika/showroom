
from django.contrib import admin
from src.supplier.models import Car, Supplier, SupplierCar


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('name', 'width', 'mileage', 'price', 'vin', 'year', 'color', 'added_date',)


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'balance', 'show_cars')

    def show_cars(self, obj):
        result = SupplierCar.objects.all().values('count').last()
        try:
            return result.get('count')
        except AttributeError:
            return None

    show_cars.short_description = "Amount cars"


@admin.register(SupplierCar)
class CarsOfSupplierAdmin(admin.ModelAdmin):
    list_display = ('count', 'discount', 'date', 'car', 'supplier')
