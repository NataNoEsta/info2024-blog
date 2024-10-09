from django.db import models

class Categoria(models.Model):

    nombre = models.CharField('Nombre categoria',max_length=200, null=False, blank=False)
    activo = models.BooleanField("Categoria Activada", default=True)
    fecha_creacion = models.DateTimeField("Fecha de Creacion", auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.nombre
