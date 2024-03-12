from django.shortcuts import render, get_object_or_404
from blog_app.models import Post

# Create your views here.
def get_all_posts(request):
    posts = Post.objects
    return render(request, 'posts.html', {'posts': posts})

def details(request, blog_id=None):
    details = get_object_or_404(Post, pk = blog_id)
    return render(request, 'details.html', {'post':details})


