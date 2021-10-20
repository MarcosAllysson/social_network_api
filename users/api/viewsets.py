from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User
from users.api.serializers import UserSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
