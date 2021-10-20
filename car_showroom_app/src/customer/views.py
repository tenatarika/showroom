from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from .serializers import GetCustomerSerializer, GetPublicSupplierSerializer, GetSupplierSerializer
from .models import Customer, Purchase



class SupplierPublicView(ModelViewSet):

    queryset = Customer.objects.all()
    serializer_class = GetCustomerSerializer
    permission_classes = [permissions.AllowAny]

    