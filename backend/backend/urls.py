from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('base.urls')),
    path('', include('blog.urls')),
    path("select2/", include("django_select2.urls")),
    path('admin/', admin.site.urls)
]
