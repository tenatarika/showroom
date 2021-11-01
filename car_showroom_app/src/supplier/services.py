from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework import permissions
from .serializers import GetCarSerializer, GetPublicSupplierSerializer, GetSupplierSerializer, SupplierPurchasesSerializer
from .models import Supplier, Car, SupplierCar
from django_filters import rest_framework as filters


class SupplierPurchasesView(ModelViewSet):
    """Suppliers purchase"""

    queryset = SupplierCar.objects.all()
    serializer_class = SupplierPurchasesSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (filters.DjangoFilterBackend, SearchFilter, OrderingFilter,)
    filter_fields = ('date', 'car', 'supplier', 'discount',)
    search_fields = ('count', 'discount', 'car', 'supplier', 'date',)
    ordering_fields = ('car', 'supplier', 'date', 'count', 'discount')


class SupplierPublicView(ReadOnlyModelViewSet):
    """View information about Suppliers"""

    queryset = Supplier.objects.all()
    serializer_class = GetPublicSupplierSerializer
    permission_classes = (permissions.AllowAny,)
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('name', 'description')


class CarPublicView(ReadOnlyModelViewSet):
    """View information about cars"""
    queryset = Car.objects.all()
    serializer_class = GetCarSerializer
    permission_classes = (permissions.AllowAny,)
    filter_backends = (filters.DjangoFilterBackend, SearchFilter, OrderingFilter,)
    filter_fields = ('mileage', 'year', 'color',)
    search_fields = ('name', 'width', 'mileage', 'price', 'year', 'color', 'vin',)
    ordering_fields = ('color', 'price', 'name', 'mileage',)


class CarView(ModelViewSet):
    """View information about cars"""
    queryset = Car.objects.all()
    serializer_class = GetCarSerializer
    permission_classes = (permissions.IsAuthenticated,)


class SupplierView(ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = GetSupplierSerializer
    permission_classes = (permissions.IsAuthenticated,)


