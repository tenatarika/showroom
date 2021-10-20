from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from .serializers import GetCarSerializer, GetPublicSupplierSerializer, GetSupplierSerializer
from .models import Supplier, Car
# Create your views here.


class SupplierPublicView(ModelViewSet):

    queryset = Supplier.objects.all()
    serializer_class = GetPublicSupplierSerializer
    permission_classes = [permissions.AllowAny]


class CarPublicView(ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = GetCarSerializer
    permission_classes = [permissions.AllowAny]


class SupplierView(ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = GetSupplierSerializer
    permission_classes = [permissions.IsAuthenticated]
