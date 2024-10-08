from django.db import models
from categorias.models import Categoria
from autores.models import Autor

# Create your models here.
class Post(models.Model):

    titulo = models.CharField(max_length=100, null=False, blank=False)
    contenido = models.TextField()
    portada = models.ImageField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    ultima_modificacion = models.DateTimeField(auto_now=True)
    activo = models.BooleanField(default=False)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    
