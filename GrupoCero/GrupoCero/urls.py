"""GrupoCero URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django import urls
from django.urls import path, include
from django.contrib import admin
from django.conf import settings

urlpatterns = [
    
    path('admin/', admin.site.urls),
    # path de artista
    path('artista/',include('artista.urls')),
    # path de contacto
    path('contact/', include('contact.urls')),
    # path del core 
    path('', include('core.urls')),
    # path de registro
    path('accounts/', include('django.contrib.auth.urls')),
    # path de api
    path('api/', include('rest_obra.urls')),
]

#si esta el debug en marcha
if settings.DEBUG:
    from django.conf.urls.static import static #importar los ficheros estaticos
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # desde la media_url que se encuentra en settings