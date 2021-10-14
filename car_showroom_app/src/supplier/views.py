from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from .serializers import GetCarSerializer, GetPublicSupplierSerializer
from .models import Supplier
# Create your views here.


class SupplierPublicView(ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = GetPublicSupplierSerializer
    permission_classes = [permissions.AllowAny]
