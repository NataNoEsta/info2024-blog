from django.urls import path
from .views import home, formulario

urlpatterns = [
    path('', home, name='home'),
    path('form_post/', formulario, name='formPost'),
]