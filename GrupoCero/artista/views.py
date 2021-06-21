from django.shortcuts import render
from .models import Artista

# artista
def artistas(request):
   artista = Artista.objects.all()
   return render(request,"artista/artistas.html",{'artistas':artista})

# detalle_artista
def detalle_artista(request):
    return render(request,"artista/detalle_artista.html")

# editar_perfil
def editar_perfil(request):
    perfil = Artista.objects.all()
    return render(request,"artista/editar_perfil.html", {'perfil':perfil})

# gestion obras
def gestion_obras(request):
    return render(request,"artista/gestion_obras.html")

# publicacion
def publicacion(request):
    return render(request,"artista/publicacion.html")

