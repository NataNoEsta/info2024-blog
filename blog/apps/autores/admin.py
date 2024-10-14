from django.contrib import admin
from .models import Autor

class AutorAdmin(admin.ModelAdmin):
    search_fields = ['nombres']
    list_display = ('nombres', 'apellidos', 'estado', 'fecha_creacion')

admin.site.register(Autor)