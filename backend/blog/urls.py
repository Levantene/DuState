from django.urls import path

from . import views

urlpatterns = [
    path('',
         views.blog,
         name='blog'),
    path('should_you_invest_in_real_estate_in_dubai/',
         views.post_one,
         name='post_one'),
    path('most_expensive_villas_in_dubai/',
         views.post_two,
         name='post_two'),
]
