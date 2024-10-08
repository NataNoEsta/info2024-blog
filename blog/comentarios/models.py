from django.db import models
from autores.models import Autor
from posts.models import Post

# Create your models here.
class Comentario(models.Model):
    
    text = models.TextField()
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)