from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

class EditarPerfil(models.Model):
    nombre_artista = models.CharField(max_length=80, verbose_name='Nombre del artista')
    pais = models.CharField(max_length=20, verbose_name='País')
    biografia = models.TextField(max_length=250, verbose_name='Biografía')
    foto_perfil = models.ImageField(verbose_name='Foto de perfil', upload_to = 'artistas')
    
    class Meta:
        verbose_name = "Perfil"
        verbose_name_plural = "Perfil"

    def __str__(self):
        return self.nombre_artista
    
class Publicacion(models.Model):
    nombre_obra = models.CharField(max_length=40,verbose_name='Nombre de la obra')
    anio = models.CharField(max_length=4, validators=[RegexValidator(r'^\d{1,4}$')],verbose_name='Año')
    precio = models.CharField(max_length=9, validators=[RegexValidator(r'^\d{1,9}$')], verbose_name='Precio ($CLP)')
    tipo_obra = models.CharField(max_length=100,verbose_name='Tipo de obra')
    alto = models.CharField(max_length=4, validators=[RegexValidator(r'^\d{1,4}$')],verbose_name='Alto (cm)')
    ancho = models.CharField(max_length=4, validators=[RegexValidator(r'^\d{1,4}$')],verbose_name='Ancho (cm)')
    largo = models.CharField(max_length=4,verbose_name='largo (cm)')
    soporte = models.CharField(max_length=20,verbose_name='Soporte (opcional)',null=True,blank=True)
    descripcion = models.TextField(max_length=250,verbose_name='Descripción')
    imagen = models.ImageField(verbose_name='Imagen', upload_to = 'obras')

    class Meta:
        verbose_name = "Obra"
        verbose_name_plural = "Obras"
    
    def __str__(self):
        return self.nombre_obra