from rest_framework import routers
from . import services


router = routers.DefaultRouter()
router.register('car', services.CarPublicView, 'Car')
router.register('supplier', services.SupplierPublicView, 'Supplier')
router.register('supplier-me', services.SupplierView, 'SupplierMe')
urlpatterns = router.urls
