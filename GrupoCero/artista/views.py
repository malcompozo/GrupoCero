from django.shortcuts import redirect, render
from .models import EditarPerfil,Publicacion
from .forms import EditarForm, PubliForm

# listando artista
def artistas(request):
    artista = EditarPerfil.objects.all()
    return render(request,"artista/artistas.html",{'artistas':artista})

# listando obras
def obras(request):
    obras = Publicacion.objects.all()
    return render(request,"artista/obras.html",{'obras':obras})




# detalle_artista
def detalle_artista(request):
    return render(request,"artista/detalle_artista.html")

# detalle_obra
def detalle_obra(request):
    return render(request,"artista/detalle_obra.html")

# gestion obras
def gestion_obras(request):
    return render(request,"artista/gestion_obras.html")

# panel
def panel(request):
    return render(request,"artista/panel.html")




# ingresar perfil
def editar_perfil(request):

    data = {
        'editForm': EditarForm()
    }

    if request.method == 'POST':
        editar = EditarForm(data=request.POST, files=request.FILES)
        if editar.is_valid():
            editar.save()
            data['mensaje'] = "Guardado correctamente"
            
        else:
            data[EditarForm] = editar
    
    return render(request,"artista/editar_perfil.html", data)

# ingresar publicacion
def publicacion(request):

    data = {
        'publiForm': PubliForm()
    }

    if request.method == 'POST':
        publicacion = PubliForm(data=request.POST, files=request.FILES)
        if publicacion.is_valid():
            publicacion.save()
            data['mensaje'] = "Guardado correctamente"
            
        else:
            data[PubliForm] = publicacion
    
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
            return redirect('panel')
    else:
        form = PubliForm(instance=editar) 
    return render(request,"artista/publicacion.html", {'editar':editar})

