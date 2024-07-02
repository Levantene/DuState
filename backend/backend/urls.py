from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('latest_transactions/', include('base.urls')),
    path('', include('blog.urls')),
    path("select2/", include("django_select2.urls")),
    path('admin/', admin.site.urls)
]
