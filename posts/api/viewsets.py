from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from posts.api.serializers import PostsSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.utils.translation import ugettext_lazy as _
from posts.models import Posts


class PostsViewSet(ModelViewSet):
    serializer_class = PostsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def list(self, request, *args, **kwargs):
        """
        GET all registers from Posts table.
        """
        posts = Posts.objects.all()
        serializer = PostsSerializer(posts, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        """
        CREATE a Post's register.
        """
        serializer = PostsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['user'] = request.user
        serializer.save()

        return Response({
            'message': _('Post created successfully'),
            'status': status.HTTP_201_CREATED
        })

    def destroy(self, request, *args, **kwargs):
        """
        DELETE a Post's register.
        """
        try:
            Posts.objects.get(pk=kwargs['pk']).delete()

        except Posts.DoesNotExist:
            return Response({'message': _('Post does not exist!')})

        else:
            return Response({
                'message': _('Post deleted successfully!'),
                'status': status.HTTP_200_OK
            })

    def retrieve(self, request, *args, **kwargs):
        """
        GET one Post register.
        """
        try:
            requested_post = Posts.objects.get(pk=kwargs['pk'])

        except Posts.DoesNotExist:
            return Response({'message': _('Post does not exist!')})

        else:
            serializer = PostsSerializer(requested_post)
            return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        """
        PUT a Post's register.
        """
        try:
            requested_post = Posts.objects.get(pk=kwargs['pk'])
            requested_post.image = request.data['image']
            requested_post.description = request.data['description']
            requested_post.user = request.user
            requested_post.save()

        except Posts.DoesNotExist:
            return Response({'message': _('Post does not exist!')})

        else:
            return Response({
                'message': _('Post successfully updated!'),
                'status': status.HTTP_200_OK
            })
