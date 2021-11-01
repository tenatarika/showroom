from rest_framework import routers
from . import services


router = routers.DefaultRouter()
router.register('car', services.CarPublicView, 'Car')
router.register('supplier', services.SupplierPublicView, 'Supplier')
router.register('supplier/purchases', services.SupplierPurchasesView, 'SupplierMe')
urlpatterns = router.urls
