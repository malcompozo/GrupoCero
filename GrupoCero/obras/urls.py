from django.urls import path
from . import views

urlpatterns = [

    path('', views.obras, name='obras'),
    path('detalle_obra/', views.obras, name='detalle_obra'),

]