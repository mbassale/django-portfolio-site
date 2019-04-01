import pkg_resources
from django.shortcuts import render, get_object_or_404
from .models import BlogPost


def home(request):
    posts = BlogPost.objects.all()
    return render(request, 'blog/home.html', {
        'posts': posts
    })


def detail(request, post_id):
    post = get_object_or_404(BlogPost, pk=post_id)
    return render(request, 'blog/detail.html', {
        'post': post
    })
