from django.db import models
from ckeditor.fields import RichTextField
from ..autores.models import Autor
from ..categorias.models import Categoria

# Create your models here.
class Post(models.Model):

    titulo = models.CharField('Titulo', max_length=100, null=False, blank=False)
    descripcion = models.CharField('Descripcion', max_length=100, blank=False, null=False)
    contenido = RichTextField()
    portada = models.ImageField()
    fecha_publicacion = models.DateTimeField('Fecha de publicacion', auto_now_add=True)
    ultima_modificacion = models.DateTimeField('Ultima modificacion', auto_now=True)
    activo = models.BooleanField(default=True)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.titulo
