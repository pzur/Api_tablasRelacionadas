from rest_framework import serializers, viewsets
from .models import Cliente, Mascota

class MascotaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Mascota
        fields = ['nombre','raza','edad','peso','sexo','tipo_animal','foto','Cliente']


class ClientesSerializer(serializers.ModelSerializer):
    dueño=serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Cliente
        fields = ['idcli','nombre','apellido','direccion','telefono','correo','foto','dueño']



