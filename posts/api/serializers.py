from rest_framework.serializers import ModelSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from posts.models import Posts


class PostsSerializer(ModelSerializer):
    class Meta:
        model = Posts
        fields = (
            'id',
            'image_path',
            'description',
            'user',
            'created',
            'modified'
        )


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token['username'] = user.username
        return token
