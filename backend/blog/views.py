from django.shortcuts import render, get_object_or_404
from .models import (
    Post,
)


def blog(request):
    posts = Post.objects.all().order_by('-pub_date')
    context = {
        'posts': posts,
        }
    return render(request, 'base/blog.html', context)


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {
        'post': post,
        }
    return render(request, 'base/post_detail.html', context)
