from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import index, about, contacto

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('', include('apps.posts.urls')),
    path('acerca/', about, name='about'),
    path('contacto/', contacto, name='contacto')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)