from django.contrib import admin
from .models import Categoria

class CategoriaAdmin(admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ('nombre', 'fecha_creacion', 'activo',)

# Register your models here.
admin.site.register(Categoria, CategoriaAdmin)
