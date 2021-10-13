from django.contrib import admin

# Register your models here.



from src.supplier.models import Supplier, Car, Supplier_Car


@admin.register(Supplier)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'balance', )

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('name', 'width', 'mileage', 'price', 'vin' )



@admin.register(Supplier_Car)
class SupplierCarAdmin(admin.ModelAdmin):
    list_display = ('count', 'discount', 'date', 'car', 'supplier' )


