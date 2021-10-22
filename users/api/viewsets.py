from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User
from users.api.serializers import UserSerializer
from users.permissions import IsSuperUser
from rest_framework.permissions import IsAdminUser


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [IsSuperUser, IsAdminUser]
    serializer_class = UserSerializer
