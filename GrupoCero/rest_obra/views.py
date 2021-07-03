import re
from django.shortcuts import render
from rest_framework import serializers, status
from rest_framework import response
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.utils.serializer_helpers import ReturnDict
from artista.models import Publicacion
from .serializers import  ObraSerializer

# Create your views here.

@csrf_exempt
@api_view(['GET','POST'])

def lista_obras(request):

    if request.method == 'GET':
        obra = Publicacion.objects.all()
        serializer = ObraSerializer(obra, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ObraSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])    
def detalle_obra(request, publicacion_id):
    try:
        obra = Publicacion.objects.get(id = publicacion_id)
    except Publicacion.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ObraSerializer(obra)
        return Response(serializer.data)
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ObraSerializer(obra, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        obra.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
        