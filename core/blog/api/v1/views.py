from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from .serializers import PostSerializer, CategorySerializer
from ...models import Post, Category
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import viewsets
from .permissions import IsOwnerOrReadOnly
from rest_framework.generics import GenericAPIView, ListCreateAPIView, ListAPIView, RetrieveAPIView , RetrieveUpdateDestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

# from rest_framework.decorators import api_view, permission_classes

# Create your views here.


# @api_view(["GET","POST"])
# @permission_classes([IsAuthenticatedOrReadOnly])
# def postList(request):
#     if request.method == "GET":
#         post = Post.objects.all()
#         Serializer = PostSerializer(post,many=True)
#         return Response(Serializer.data)
#     elif request.method == "POST":
#         Serializer = PostSerializer(data=request.data)
#         if Serializer.is_valid():
#             Serializer.save()
#             return Response(Serializer.date)
#         else:
#             return Response(Serializer.errors)

'''class PostList(APIView):
    """
    getting a list of posts and creating new posts
    """
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer

    def get(self, request):
        """
        retriveing a list of posts
        """
        post = Post.objects.all()
        Serializer = PostSerializer(post,many=True)
        return Response(Serializer.data)

    def post(self, request):
        """
        creating a post with provided data
        """
        Serializer = PostSerializer(data=request.data)
        if Serializer.is_valid():
            Serializer.save()
            return Response(Serializer.date)
        else:
            return Response(Serializer.errors)'''


class PostList(ListCreateAPIView):
    """
    getting a list of posts and creating new posts
    """
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    
# viewsets.ViewSet
'''class PostViewset(viewsets.ViewSet):
    """A Simple Viewset for listing or retrieving users"""
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    # lookup_field = 'id'
    

    def list (self, request):
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve (self, request, pk=None):
        post_object = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(post_object)
        return Response(serializer.data)'''

class PostModelViewset(viewsets.ModelViewSet):
    """A Simple Viewset for listing or retrieving users"""
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category', 'status', 'author']
    search_fields = ['title', 'content']
    ordering_fields = ['published_date']

class CategoryModelViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
        
            

# @api_view(["GET","PUT","DELETE"])
# def postDetail(request,id):
#     post = Post.objects.get(pk = id)
#     if request.method == "GET":
#         try:
#             Serializer = PostSerializer(post)
#             return Response(Serializer.data)
#         except Post.DoesNotExist:
#             return Response({"detail":"objects does not exist"},status=404)
#     elif request.method == "PUT":
#         Serializer = PostSerializer(post, data=request.data)
#         Serializer.is_valid(raise_exception=True)
#         Serializer.save()
#         return Response(Serializer.data)
#     elif request.method == "DELETE":
#         post.delete()
#         return Response({"detail":"item removed successfully"},status=204)


'''class PostDetail(APIView):
    """
    getting detail of the posts and edit remove it
    """
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer

    def get(self, request, id):
        """ retriveing the post data """
        post = Post.objects.get(pk = id)
        try:
            Serializer = self.serializer_class(post)
            return Response(Serializer.data)
        except Post.DoesNotExist:
            return Response({"detail":"objects does not exist"},status=404)

    def put(self, request, id):
        """ editing the post data """
        post = Post.objects.get(pk = id)
        Serializer = self.serializer_class(post, data=request.data)
        Serializer.is_valid(raise_exception=True)
        Serializer.save()
        return Response(Serializer.data)
    
    def delete(self, request, id):
        """ delete the post data """
        post = Post.objects.get(pk = id)
        post.delete()
        return Response({"detail":"item removed successfully"},status=204)'''


# GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin
'''class PostDetail(GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    """ getting detail of the posts and edit remove it """
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        """ retriveing the post data """
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        """ update the post data """
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        """ dalete the post data """
        return self.destroy(request, *args, **kwargs)'''

#all in one
class PostDetail(RetrieveUpdateDestroyAPIView):
    """ getting detail of the posts and edit remove it """
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    lookup_field = 'id'
