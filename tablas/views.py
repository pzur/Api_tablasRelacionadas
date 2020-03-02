from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from .models import Cliente, Mascota
from .serializer import ClientesSerializer,MascotaSerializer
from rest_framework import viewsets

# Create your views here.


class ClienteList(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClientesSerializer


class MascotaList(viewsets.ModelViewSet):
    queryset = Mascota.objects.all()
    serializer_class = MascotaSerializer







