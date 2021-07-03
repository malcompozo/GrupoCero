from django import urls
from django.urls import path
from rest_obra.views import lista_obras

urlpatterns = [
    path('lista_obras', lista_obras, name='lista_obras'),
]