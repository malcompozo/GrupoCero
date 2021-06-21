from django.shortcuts import render
from .models import EditarPerfil,Publicacion

# artista
def artistas(request):
    artista = EditarPerfil.objects.all()
    return render(request,"artista/artistas.html",{'artistas':artista})

# detalle_artista
def detalle_artista(request):
    return render(request,"artista/detalle_artista.html")

# detalle_obra
def detalle_obra(request):
    return render(request,"artista/detalle_obra.html")

# editar_perfil
def editar_perfil(request):
    perfil = EditarPerfil.objects.all()
    return render(request,"artista/editar_perfil.html", {'perfil':perfil})

# gestion obras
def gestion_obras(request):
    return render(request,"artista/gestion_obras.html")

# obras
def obras(request):
    obras = Publicacion.objects.all()
    return render(request,"artista/obras.html",{'Publicacion':obras})

# panel
def panel(request):
    return render(request,"artista/panel.html")

# publicacion
def publicacion(request):
    return render(request,"artista/publicacion.html")


