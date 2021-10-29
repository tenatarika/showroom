from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework import permissions
from .serializers import GetCarSerializer, GetPublicSupplierSerializer, GetSupplierSerializer, SupplierPurchasesSerializer
from .models import Supplier, Car, SupplierCar
# Create your views here.


class SupplierPurchasesView(ModelViewSet):
    """Suppliers purchase"""

    queryset = SupplierCar.objects.all()
    serializer_class = SupplierPurchasesSerializer
    permission_classes = (permissions.IsAuthenticated,)


class SupplierPublicView(ReadOnlyModelViewSet):
    """View information about Suppliers"""

    queryset = Supplier.objects.all()
    serializer_class = GetPublicSupplierSerializer
    permission_classes = (permissions.AllowAny,)


class CarPublicView(ReadOnlyModelViewSet):
    """View information about cars"""
    queryset = Car.objects.all()
    serializer_class = GetCarSerializer
    permission_classes = (permissions.AllowAny,)


class CarView(ModelViewSet):
    """View information about cars"""
    queryset = Car.objects.all()
    serializer_class = GetCarSerializer
    permission_classes = (permissions.IsAuthenticated,)


class SupplierView(ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = GetSupplierSerializer
    permission_classes = (permissions.IsAuthenticated,)



