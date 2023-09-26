from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer

from .producer import publish 

class PostViewSet(viewsets.ViewSet):
    def list(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        publish('post_created',serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        product = Post.objects.get(id=pk)
        serializer = PostSerializer(product)
        return Response(serializer.data)

    def update(self, request, pk=None):
        product = Post.objects.get(id=pk)
        serializer = PostSerializer(instance=product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        publish('post_updated',serializer.data)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        product = Post.objects.get(id=pk)
        product.delete()
        publish('post_deleted', pk)
        return Response(status=status.HTTP_204_NO_CONTENT)
