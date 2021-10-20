from django.urls import  path
from . import views


urlpatterns = [
    path('showroom/<int:pk>/', views.ShowroomPublicView.as_view(
        {'get': 'retrieve'})),
    path('showroom/get_cars/<int:pk>/', views.ShowroomView.as_view(
        {'get': 'retrieve', 'put': 'update'})),
]