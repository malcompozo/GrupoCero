from django import urls
from django.urls import path
from rest_obra.views import lista_obras,detalle_obra
from rest_obra.viewslogin import login_api

urlpatterns = [
    path('lista_obras', lista_obras, name='lista_obras'),
    path('detalle_obra/<publicacion_id>', detalle_obra, name='detalle_obra'),
    path('login_api', login_api, name='login_api'),
]