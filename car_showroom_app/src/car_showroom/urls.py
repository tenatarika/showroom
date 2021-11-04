from rest_framework import routers
from . import  views

router = routers.DefaultRouter()
router.register('', views.ShowroomPublicView, 'CarShowroom')
router.register('get_cars', views.ShowroomView, 'CarsOfShowroom')
urlpatterns = router.urls

