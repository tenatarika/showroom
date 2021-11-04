from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register('car', views.CarPublicView, 'Car')
router.register('supplier', views.SupplierPublicView, 'Supplier')
router.register('supplier/purchases', views.SupplierPurchasesView, 'SupplierMe')
urlpatterns = router.urls
