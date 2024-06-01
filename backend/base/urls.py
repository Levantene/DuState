from django.urls import path

from . import views
from base.views import ajax_view

urlpatterns = [
    path('', views.index, name='index'),
    path('line_data/', views.line_data, name='line-data'),
    path('bar_data/', views.bar_data, name='bar-data'),
    path(r'^ajax/$', ajax_view.as_view(), name='ajax_url'),
    path('load_project_names/',
         views.load_project_names,
         name='load_project_names'),
    path('load_building_names/',
         views.load_building_names,
         name='load_building_names'),
    path('load_rooms_number/',
         views.load_rooms_number,
         name='load_rooms_number'),
    path('all_transactions/',
         views.all_transactions,
         name='all-transactions'),
]
