from django import forms
from django.forms import widgets
from .models import EditarPerfil, Publicacion

class EditarForm(forms.ModelForm):
    class Meta:
        model = EditarPerfil
        fields = '__all__'

        widgets = {
            'nombre_artista': forms.TextInput(attrs={'class':'form-control'}),
            'pais': forms.TextInput(attrs={'class':'form-control'}),
            'biografia': forms.Textarea(attrs={'class':'form-control'}),
        }
        
class PubliForm(forms.ModelForm):
    class Meta:
        model = Publicacion
        fields = '__all__'

        widgets = {
            'nombre_obra': forms.TextInput(attrs={'class':'form-control'}),
            'anio': forms.NumberInput(attrs={'class':'form-control'}),
            'precio': forms.NumberInput(attrs={'class':'form-control'}),
            'tipo_obra': forms.TextInput(attrs={'class':'form-control'}),
            'alto': forms.NumberInput(attrs={'class':'form-control'}),
            'ancho': forms.NumberInput(attrs={'class':'form-control'}),
            'largo': forms.NumberInput(attrs={'class':'form-control'}),
            'soporte': forms.TextInput(attrs={'class':'form-control'}),
            'descripcion': forms.Textarea(attrs={'class':'form-control'}),
        }
    