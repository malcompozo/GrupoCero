from django.urls import path
from . import views

urlpatterns = [

    path('', views.obras, name='obras'),
    path('detalle_obra/', views.detalle_obra, name='detalle_obra'),

]