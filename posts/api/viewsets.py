from rest_framework.viewsets import ModelViewSet
from posts.api.serializers import PostsSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from posts.models import Posts


class PostsViewSet(ModelViewSet):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer
    permission_classes = [AllowAny]
