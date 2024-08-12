from django.shortcuts import render
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
                  'blog/most_expensive_villas_in_dubai.html',
                  context)


def post_three(request):
    context = {}
    return render(request,
                  'blog/best_areas_for_investment_in_dubai.html',
                  context)
