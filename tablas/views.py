from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from .models import Cliente, Mascota, Paseador
from rest_framework import viewsets
from .serializer import ClientesSerializer,MascotaSerializer, PaseadorSerializer

# Create your views here.


class ClienteList(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClientesSerializer


class MascotaList(viewsets.ModelViewSet):
    queryset = Mascota.objects.all()
    serializer_class = MascotaSerializer

class PaseadorList(viewsets.ModelViewSet):
    queryset = Paseador.objects.all()
    serializer_class = PaseadorSerializer







