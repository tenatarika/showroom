from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from .serializers import GetCustomerSerializer, GetPrivateCustomerSerializer, GetPurchaseSerializer
from .models import Customer, Purchase


class CustomerPublicView(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = GetCustomerSerializer
    permission_classes = (permissions.AllowAny,)


class CustomerPrivateView(ModelViewSet):

    serializer_class = GetPrivateCustomerSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Customer.objects.filter(id=self.request.user.id)


class PurchaseView(ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = GetPurchaseSerializer
    permission_classes = (permissions.IsAuthenticated,)
