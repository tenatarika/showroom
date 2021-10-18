from django.urls import  path
from . import views

urlpatterns = [
    
    path('supplier/<int:pk>/', views.SupplierPublicView.as_view({'get': 'retrieve'})),
    path('car/<int:pk>/', views.CarPublicView.as_view({'get': 'retrieve'})),
    path('supplier/me/<int:pk>/', views.SupplierView.as_view({'get': 'retrieve', 'put': 'update'})),
]