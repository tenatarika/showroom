from rest_framework import routers
from . import services


router = routers.DefaultRouter()
router.register('', services.ShowroomPublicView, 'CarShowroom')
router.register('get_cars', services.ShowroomView, 'CarsOfShowroom')
urlpatterns = router.urls

