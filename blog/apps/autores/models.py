from django.db import models

class Autor(models.Model):
    
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    email = models.EmailField(unique=True, null=False, blank=False)
