from django.urls import path
from . import views

urlpatterns = [

    path('', views.artistas, name='artistas'),
    path('detalle_artista/', views.detalle_artista, name='detalle_artista'),
    path('editar_perfil/', views.editar_perfil, name='editar_perfil'),
    path('gestion_obras/', views.gestion_obras, name='gestion_obras'),
    path('publicacion/', views.publicacion, name='publicacion'),
    path('panel/', views.panel, name='panel'),

]