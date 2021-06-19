from django.shortcuts import render

# index
def index(request):
    return render(request,"core/index.html")

# crear_cuenta
def crear_cuenta(request):
    return render(request,"core/crear_cuenta.html")

# publicacion
def publicacion(request):
    return render(request,"core/publicacion.html")

# login
def login(request):
    return render(request,"core/login.html")

# gestion_obras
def gestion_obras(request):
    return render(request,"core/gestion_obras.html")

# panel
def panel(request):
    return render(request,"core/panel.html")