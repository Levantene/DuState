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


def post_one(request):
    context = {}
    return render(request,
                  'blog/should_you_invest_in_real_estate_in_dubai.html',
                  context)


def post_two(request):
    context = {}
    return render(request,
                  'blog/Most_expensive_villas_in_dubai.html',
                  context)
