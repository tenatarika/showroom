from django.contrib import admin
from src.customer.models import Customer, Purchase, Location
from django.db.models import Avg


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('country', 'city', 'street', 'house_num',)


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'phone', 'birthday', 'balance', 'location', 'show_average')

    def show_average(self, obj):
        result = Purchase.objects.filter(
            customer=obj).aggregate(Avg("discount"))

        return result.get("discount__avg")


    show_average.short_description = "Average discount"


@admin.register(Purchase)
class CustomerPurchaseAdmin(admin.ModelAdmin):
    list_display = ('car', 'count', 'car_showroom', 'discount')
