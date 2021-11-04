from rest_framework import routers

from src.car_showroom import views


router = routers.DefaultRouter()
router.register('', views.ShowroomPublicView, 'CarShowroom')
router.register('showroom_cars', views.ShowroomView, 'CarsOfShowroom')
urlpatterns = router.urls
