from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import permissions
from django_filters import rest_framework as filters

from src.customer.models import Customer, Purchase
from src.customer.serializers import GetCustomerSerializer, GetPrivateCustomerSerializer
from src.customer.serializers import GetPurchaseSerializer


class CustomerPublicView(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = GetCustomerSerializer
    permission_classes = (permissions.AllowAny,)
    filter_backends = (filters.DjangoFilterBackend, SearchFilter, OrderingFilter,)
    filter_fields = ('name', 'gender', 'birthday',)
    search_fields = ('sample', 'location', 'car', 'name', 'birthday',)
    ordering_fields = ('sample', 'location', 'birthday', 'name',)


class CustomerPrivateView(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = GetPrivateCustomerSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (filters.DjangoFilterBackend, SearchFilter, OrderingFilter,)
    filter_fields = ('name', 'gender',  'birthday', 'phone',)
    search_fields = ('sample', 'location', 'car', 'name', 'birthday', 'phone',)
    ordering_fields = ('sample', 'location', 'birthday', 'name', 'phone',)


class PurchaseView(ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = GetPurchaseSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (filters.DjangoFilterBackend, SearchFilter, OrderingFilter,)
    filter_fields = ('car', 'car_showroom', 'discount',)
    search_fields = ('car', 'car_showroom', 'discount',)
    ordering_fields = ('car', 'car_showroom', 'discount',)
