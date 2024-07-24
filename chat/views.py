from rest_framework import viewsets

from chat.models import User
from chat.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    model = User
    serializer_class = UserSerializer
