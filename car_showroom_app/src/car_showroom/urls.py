from django.urls import  path
from . import views


urlpatterns = [
    path('<int:pk>/', views.ShowroomPublicView.as_view(
        {'get': 'retrieve'})),
    path('get_cars/<int:pk>/', views.ShowroomView.as_view(
        {'get': 'retrieve', 'put': 'update'})),
]