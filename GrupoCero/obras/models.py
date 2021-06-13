from django.db import models

# Create your models here.

class Obra(models.Model):
    nombre_obra = models.CharField(max_length=40,verbose_name='Nombre de la obra')
    anio = models.CharField(max_length=4,verbose_name='Año')
    precio = models.CharField(max_length=9, verbose_name='Precio ($CLP)')
    tipo_obra = models.CharField(max_length=20,verbose_name='Tipo de obra')
    alto = models.CharField(max_length=4,verbose_name='Alto')
    ancho = models.CharField(max_length=4,verbose_name='Ancho')
    largo = models.CharField(max_length=4,verbose_name='largo')
    soporte = models.CharField(max_length=20,verbose_name='Soporte')
    descripcion = models.TextField(max_length=250,verbose_name='Descripción')
    imagen = models.ImageField(verbose_name='Imagen', upload_to = 'obras')


    class Meta:
        verbose_name = "Obra"
        verbose_name_plural = "Obras"
    
    def __str__(self):
        return self.nombre_obra