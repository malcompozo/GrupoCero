from django.shortcuts import render
from .models import Obra

# obras
def obras(request):
    obras = Obra.objects.all()
    return render(request,"obras/obras.html",{'obras':obras})

# detalle_obra
def detalle_obra(request):
    return render(request,"obras/detalle_obra.html")
