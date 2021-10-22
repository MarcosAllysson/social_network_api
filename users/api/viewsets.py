from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from users.api.serializers import UserSerializer
from users.permissions import IsSuperUser
from rest_framework.permissions import IsAdminUser


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [IsSuperUser, IsAdminUser]
    serializer_class = UserSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
