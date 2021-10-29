from rest_framework import routers
from . import services


router = routers.DefaultRouter()
router.register('', services.CustomerPrivateView, 'Customer')
router.register('purchase', services.PurchaseView, 'Purchase')
urlpatterns = router.urls
