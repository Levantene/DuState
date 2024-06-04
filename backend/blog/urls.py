from django.urls import path

from . import views

urlpatterns = [
    path('blog/',
         views.blog,
         name='blog'),
    path('blog/should_you_invest_in_real_estate_in_dubai/',
         views.post_one,
         name='post_one'),
    path('blog/most_expensive_villas_in_dubai/',
         views.post_two,
         name='post_two'),
]
