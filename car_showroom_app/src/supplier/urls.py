from django.urls import  path
from . import views

urlpatterns = [
    # path('supplier/<int:pk>/', views.UserNetView.as_view({'get': 'retrieve', 'put': 'update'})),
    path('<int:pk>/', views.SupplierPublicView.as_view({'get': 'retrieve'})),
]