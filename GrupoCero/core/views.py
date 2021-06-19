from django.shortcuts import render

# index
def index(request):
    return render(request,"core/index.html")

# artista
def artistas(request):
    return render(request,"core/artistas.html")

# crear_cuenta
def crear_cuenta(request):
    return render(request,"core/crear_cuenta.html")

# detalle_artista
def detalle_artista(request):
    return render(request,"core/detalle_artista.html")

# detalle_obra
def detalle_obra(request):
    return render(request,"core/detalle_obra.html")

# publicacion
def publicacion(request):
    return render(request,"core/publicacion.html")

# login
def login(request):
    return render(request,"core/login.html")

# gestion_obras
def gestion_obras(request):
    return render(request,"core/gestion_obras.html")

# editar_perfil
def editar_perfil(request):
    return render(request,"core/editar_perfil.html")

# panel
def panel(request):
    return render(request,"core/panel.html")