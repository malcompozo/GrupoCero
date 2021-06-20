from django.db import models

# Create your models here.

class Artista(models.Model):
    nombre_artista = models.CharField(max_length=80, verbose_name='Nombre del artista')
    especialidad_artista = models.CharField(max_length=80, verbose_name='Especialidad')
    biografia = models.TextField(max_length=250, verbose_name='Biografía')
    pais = models.CharField(max_length=20, verbose_name='País')
    foto_perfil = models.ImageField(verbose_name='Foto de perfil', upload_to = 'artistas')

    def __str__(self):
        return self.nombre_artista