from rest_framework import routers

from src.customer import views

router = routers.DefaultRouter()
router.register('', views.CustomerPrivateView, 'Customer')
router.register('purchase', views.PurchaseView, 'Purchase')
urlpatterns = router.urls
