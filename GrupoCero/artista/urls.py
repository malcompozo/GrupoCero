from django.urls import path
from . import views

urlpatterns = [

    path('', views.artistas, name='artistas'),
    path('detalle_artista/<int:artista_id>/', views.detalle_artista, name='detalle_artista'),
    path('detalle_obra/<int:publi_id>/', views.detalle_obra, name='detalle_obra'),
    path('editar_perfil/', views.editar_perfil, name='editar_perfil'),
    path('gestion_obras/', views.gestion_obras, name='gestion_obras'),
    path('obras/', views.obras, name='obras'),
    path('panel/', views.panel, name='panel'),
    path('publicacion/', views.publicacion, name='publicacion'),
    path('eliminar/<int:publicacion_id>/', views.eliminar, name='eliminar'),
    path('editar/<int:publicacion_id>/', views.editar, name='editar'),

]