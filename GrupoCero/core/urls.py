from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('crear_cuenta/', views.crear_cuenta, name='crear_cuenta'),
    path('login/', views.login, name='login'),
    path('publicacion/', views.publicacion, name='publicacion'),
    path('gestion_obras/', views.gestion_obras, name='gestion_obras'),
    path('panel/', views.panel, name='panel'),
]
