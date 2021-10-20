from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from .serializers import GetPublicShowroom, GetCarsOfShowroom
from .models import CarShowroom, CarsOfShowroom


class ShowroomPublicView(ModelViewSet):
    queryset = CarShowroom.objects.all()
    serializer_class = GetPublicShowroom
    permission_classes = [permissions.AllowAny]


class ShowroomView(ModelViewSet):
    queryset = CarsOfShowroom.objects.all()
    serializer_class = GetCarsOfShowroom
    permission_classes = [permissions.IsAuthenticated]
