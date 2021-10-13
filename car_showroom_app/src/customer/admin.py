from django.contrib import admin
from src.customer.models import Customer, Purchase


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'birthday', 'balance', 'country' )


@admin.register(Purchase)
class CustomerPurchaseAdmin(admin.ModelAdmin):
    list_display = ('car', 'supplier', 'car_showroom', 'discount')



