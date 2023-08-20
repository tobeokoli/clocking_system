from rest_framework import viewsets, mixins
from .models import CustomUser
from .serializers import UserRegistrationSerializer

class UserRegistrationViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserRegistrationSerializer