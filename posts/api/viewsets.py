from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from posts.api.serializers import PostsSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.utils.translation import ugettext_lazy as _
from posts.models import Posts


class PostsViewSet(ModelViewSet):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def list(self, request, *args, **kwargs):
        """
        GET all registers from Posts table.
        """
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
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
            status: status.HTTP_201_CREATED
        })

    def destroy(self, request, *args, **kwargs):
        """
        DELETE a Post's register.
        """
        try:
            requested_post = Posts.objects.get(pk=kwargs['pk'])

            if requested_post.user == request.user:
                requested_post.delete()

                return Response({
                    'message': _('Post deleted successfully!'),
                    status: status.HTTP_200_OK
                })

            else:
                return Response({
                    'message': _('You do not have permission to delete this post!'),
                    status: status.HTTP_403_FORBIDDEN
                })

        except Posts.DoesNotExist:
            return Response({
                'message': _('Post does not exist!'),
                status: status.HTTP_404_NOT_FOUND
            })

    def retrieve(self, request, *args, **kwargs):
        """
        GET one Post register.
        """
        try:
            requested_post = Posts.objects.get(pk=kwargs['pk'])
            serializer = PostsSerializer(requested_post)
            return Response(serializer.data, status.HTTP_200_OK)

        except Posts.DoesNotExist:
            return Response({
                'message': _('Post does not exist!'),
                status: status.HTTP_404_NOT_FOUND
            })

    def update(self, request, *args, **kwargs):
        """
        PUT a Post's register.
        """
        try:
            requested_post = Posts.objects.get(pk=kwargs['pk'])

            if requested_post.user == request.user:
                requested_post.image = request.data['image']
                requested_post.description = request.data['description']
                requested_post.user = request.user
                requested_post.save()

                return Response({
                    'message': _('Post successfully updated!'),
                    status: status.HTTP_200_OK
                })

            else:
                return Response({
                    'message': _('You do not have permission to update this post!'),
                    status: status.HTTP_403_FORBIDDEN
                })

        except Posts.DoesNotExist:
            return Response({
                'message': _('Post does not exist!'),
                status: status.HTTP_404_NOT_FOUND
            })
