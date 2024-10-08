from django.db import models

# Create your models here.
class Post(models.Model):

    titulo = models.CharField(max_length=100, null=False, blank=False)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    ultima_modificacion = models.DateTimeField(auto_now=True)
    
