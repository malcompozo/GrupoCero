from django.urls import path
from . import views

urlpatterns = [

    path('', views.artistas, name='artistas'),
    path('detalle_artista/', views.detalle_artista, name='detalle_artista'),
    path('editar_perfil/', views.editar_perfil, name='editar_perfil'),

]