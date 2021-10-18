from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from .serializers import GetPublicShowroom, GetCarsOfShowroom
from .models import Car_showroom, Car_showroom_Car



class ShowroomPublicView(ModelViewSet):
    queryset = Car_showroom.objects.all()
    serializer_class = GetPublicShowroom
    permission_classes = [permissions.AllowAny]

# Create your views here.

class ShowroomView(ModelViewSet):
    queryset = Car_showroom_Car.objects.all()
    serializer_class = GetCarsOfShowroom
    permission_classes = [permissions.IsAuthenticated]