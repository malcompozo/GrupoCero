from rest_framework import fields, serializers
from artista.models import Publicacion

class ObraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publicacion
        fields = '__all__'