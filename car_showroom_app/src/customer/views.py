from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from .serializers import GetCustomerSerializer, GetPrivateCustomerSerializer
from .models import Customer


class CustomerPublicView(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = GetCustomerSerializer
    permission_classes = [permissions.AllowAny]


class CustomerPrivateView(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = GetPrivateCustomerSerializer
    permission_classes = [permissions.IsAuthenticated]
