from django import forms
from .models import EditarPerfil, Publicacion

class EditarForm(forms.ModelForm):
    class Meta:
        model = EditarPerfil
        fields = ['nombre_artista', 'pais', 'biografia', 'foto_perfil']
        
class PubliForm(forms.ModelForm):
    class Meta:
        model = Publicacion
        fields = ['nombre_obra', 'anio', 'precio', 'tipo_obra', 'alto', 'ancho', 'largo', 'soporte', 'descripcion', 'imagen']
    