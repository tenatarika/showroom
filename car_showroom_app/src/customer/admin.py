from django.contrib import admin
from src.customer.models import Customer, Purchase
from django.db.models import Avg


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'phone', 'birthday', 'balance', 'country', 'show_average',)

    def show_average(self, obj):
        result = Purchase.objects.filter(
            supplier=obj).aggregate(Avg("discount"))
        return result["discount__avg"]

    show_average.short_description = "Average discount"


@admin.register(Purchase)
class CustomerPurchaseAdmin(admin.ModelAdmin):
    list_display = ('car', 'supplier', 'car_showroom', 'discount',)
