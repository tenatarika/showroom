from django.urls import  path
from . import views

urlpatterns = [
    path('<int:pk>/', views.CustomerPublicView.as_view(
        {'get': 'retrieve'})),
    path('me/<int:pk>/', views.CustomerPrivateView.as_view(
        {'get': 'retrieve', 'put': 'update',  'delete': 'destroy'})),
    path('me/purchase/<int:pk>/', views.PurchaseView.as_view(
        {'get': 'retrieve', 'put': 'update'})),
]