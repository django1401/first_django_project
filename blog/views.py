from django.shortcuts import render
from .models import Post



def blog_home(req):
    posts = Post.objects.filter(status=True,published_date__gte='2023-05-06')
    context = {
        'posts' : posts
    }
    return render(req, 'blog/blog-home.html', context=context)