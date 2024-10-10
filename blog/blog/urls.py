from django.contrib import admin
from django.urls import path, include
from .views import index

urlpatterns = [
    path('', include('apps.posts.urls')),
    path('admin/', admin.site.urls),
]
