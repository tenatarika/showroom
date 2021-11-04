from django.contrib import admin
from src.customer.models import Customer, Purchase, Location
from django.db.models import Avg


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('country', 'city', 'street', 'houseNum',)


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'phone', 'birthday', 'balance', 'location', 'show_average')

    def show_average(self, obj):
        result = Purchase.objects.filter(
            supplier=obj).aggregate(Avg("discount"))
        try:
            return result["discount__avg"]
        except AttributeError:
            return None

    show_average.short_description = "Average discount"


@admin.register(Purchase)
class CustomerPurchaseAdmin(admin.ModelAdmin):
    list_display = ('car', 'supplier', 'car_showroom', 'discount')
