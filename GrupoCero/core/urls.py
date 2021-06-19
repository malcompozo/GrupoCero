from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('artistas/', views.artistas, name='artistas'),
    path('crear_cuenta/', views.crear_cuenta, name='crear_cuenta'),
    path('detalle_artista/', views.detalle_artista, name='detalle_artista'),
    path('detalle_obra/', views.detalle_obra, name='detalle_obra'),
    path('login/', views.login, name='login'),
    path('publicacion/', views.publicacion, name='publicacion'),
    path('gestion_obras/', views.gestion_obras, name='gestion_obras'),
    path('editar_perfil/', views.editar_perfil, name='editar_perfil'),
    path('panel/', views.panel, name='panel'),
]
