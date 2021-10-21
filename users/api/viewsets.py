from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User
from users.api.serializers import UserSerializer
from rest_framework.permissions import IsAdminUser


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = UserSerializer

    # def get_queryset(self):
    #     return User.objects.filter(is_active=True)
