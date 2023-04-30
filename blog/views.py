from django.shortcuts import render
from .models import Post

# Create your views here.



def blog_home(req):
    posts = Post.objects.filter(status=True)
    context = {
        'posts' : posts
    }
    return render(req, 'blog/blog-home.html', context=context)