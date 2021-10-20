from rest_framework.viewsets import ModelViewSet
from posts.api.serializers import PostsSerializer
from posts.models import Posts


class PostsViewSet(ModelViewSet):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer
