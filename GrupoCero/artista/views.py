from django.shortcuts import render
from .models import Artista

# artista
#def artista(request):
#   artista = Artista.objects.all()
#  return render(request,"artista/artista.html",{'artista':artista})


# detalle_artista
def detalle_artista(request):
    return render(request,"artista/detalle_artista.html")

    
# artista
def artistas(request):
    return render(request,"artista/artistas.html")

# editar_perfil
def editar_perfil(request):
    perfil = Artista.objects.get()
    return render(request,"core/editar_perfil.html", {'perfil':perfil})