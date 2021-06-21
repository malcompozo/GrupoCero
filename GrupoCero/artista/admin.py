from django.contrib import admin
from .models import EditarPerfil, Publicacion

# Register your models here.

admin.site.register([EditarPerfil, Publicacion])