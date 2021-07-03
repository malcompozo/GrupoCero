from django.shortcuts import redirect, render
from .models import EditarPerfil,Publicacion
from .forms import EditarForm, PubliForm
from django.urls import reverse

# listando artista
def artistas(request):
    artista = EditarPerfil.objects.all()
    return render(request,"artista/artistas.html",{'artista':artista})

# listando obras
def obras(request):
    obras = Publicacion.objects.all()
    return render(request,"artista/obras.html",{'obras':obras})

# listando obras en gestion obras
def gestion_obras(request):
    obras = Publicacion.objects.all()
    return render(request,"artista/gestion_obras.html",{'obras':obras})



# detalle_artista
def detalle_artista(request, artista_id):
    artista = EditarPerfil.objects.get(rut_artista=artista_id)
    obras = Publicacion.objects.all().filter(autor_id=artista_id)
    return render(request,"artista/detalle_artista.html", {'artista': artista, 'obras':obras})

# detalle_obra
def detalle_obra(request, publi_id):
    obras = Publicacion.objects.get(id=publi_id)

    return render(request,"artista/detalle_obra.html", {'obras':obras})

# panel
def panel(request):
    return render(request,"artista/panel.html")



# CRUD

# AGREGAR PERFIL
def editar_perfil(request):

    data = {
        'editForm': EditarForm()
    }

    if request.method == 'POST':
        editar = EditarForm(data=request.POST, files=request.FILES)
        if editar.is_valid():
            editar.save()
            return redirect(reverse('editar_perfil')+"?ok")
            
        else:
            data[EditarForm] = editar
            return redirect(reverse('editar_perfil')+"?fail")
    
    return render(request,"artista/editar_perfil.html", data)

# AGREGAR PUBLICACION
def publicacion(request):

    data = {
        'publiForm': PubliForm()
    }

    if request.method == 'POST':
        publicacion = PubliForm(data=request.POST, files=request.FILES)
        if publicacion.is_valid():
            publicacion.save()
            return redirect(reverse('publicacion')+"?ok")
            
        else:
            data[PubliForm] = publicacion
            return redirect(reverse('publicacion')+"?fail")
        
    return render(request,"artista/publicacion.html", data)

# ELIMINAR
def eliminar(request, publicacion_id):
    eliminar = Publicacion.objects.get(id=publicacion_id)
    eliminar.delete()
    return redirect ("gestion_obras")

# EDITAR
def editar(request, publicacion_id):
    editar = Publicacion.objects.get(id=publicacion_id)
    if request.method == 'POST':
        form = PubliForm(request.POST, instance=editar)
        if form.is_valid():
            form.save()
            return redirect(reverse('gestion_obras')+"?ok")
    else:
        form = PubliForm(instance=editar)
    
    return render(request,"artista/editar.html", {'form':form})


