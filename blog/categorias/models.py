from django.db import models

class Categoria(models.Model):

    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.nombre
