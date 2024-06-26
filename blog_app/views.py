from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from blog_app.models import Post
from blog_app.serializers import PostSerializer
from blog_app.permissions import IsPostPossessor
from blog_app.filters import PostFilter



# Create your views here.
def get_all_posts(request):
    posts = Post.objects
    return render(request, 'posts.html', {'posts': posts})

def details(request, blog_id=None):
    details = get_object_or_404(Post, pk = blog_id)
    return render(request, 'details.html', {'post':details})

# Hello world using REST API
class helloWorldView(APIView):

    def get(self, request):
        return Response({'message':'Hello World!'})
    
class PostView(ModelViewSet):
    permission_classes = [IsAuthenticated, IsPostPossessor]
    #queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filter_class = PostFilter
    ordering_fields = ['id']
    search_fields = ['title', 'body']

    def get_queryset(self):
        return Post.objects.filter(created_by=self.request.user)



