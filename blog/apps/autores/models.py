from django.db import models

class Autor(models.Model):
    
    nombres = models.CharField('Nombre de autor', max_length=255, null=False, blank=False)
    apellidos = models.CharField('Apellidos de autor', max_length=255, null=False, blank=False)
    correo = models.EmailField('Correo electronico', null=False, blank=False, unique=True)
    estado = models.BooleanField('Autor Activo', default=True)
    fecha_creacion = models.DateTimeField('Fecha de creacion', auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    def __str__(self):
        return f'{self.apellidos}, {self.nombres}'
