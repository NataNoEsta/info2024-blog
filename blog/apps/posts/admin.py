from django.contrib import admin

from ..autores.models import Autor
from .models import Post

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "titulo", "contenido")

admin.site.register(Autor)
# admin.site.register(Categoria)