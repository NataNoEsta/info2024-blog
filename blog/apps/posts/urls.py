from django.urls import path
from .views import home, formulario
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', home, name='home'),
    path('form_post/', formulario, name='formPost'),
    
]