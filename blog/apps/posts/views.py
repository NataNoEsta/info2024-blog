from django.shortcuts import render
from .models import Post
from .forms import PostForm

def home(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'pagina_principal.html', context=context)


def formulario(request):
    form = PostForm()

    context = {'form': form}
    return render(request, 'formulario_post.html', context)