from rest_framework.serializers import ModelSerializer
from posts.models import Posts


class PostsSerializer(ModelSerializer):
    class Meta:
        model = Posts
        fields = (
            'id',
            'image',
            'description',
            'user',
            'created',
            'modified'
        )
