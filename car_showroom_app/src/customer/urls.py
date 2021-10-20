from django.urls import  path
from . import views

urlpatterns = [
    path('customer/<int:pk>/', views.CustomerPublicView.as_view(
        {'get': 'retrieve'})),
    path('customer/me/<int:pk>/', views.CustomerPrivateView.as_view(
        {'get': 'retrieve', 'put': 'update'})),
]