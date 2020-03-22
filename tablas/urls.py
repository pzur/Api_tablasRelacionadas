from django.urls import path,include
from .import views
from rest_framework import routers

routers=routers.DefaultRouter()
routers.register('Cliente',views.ClienteList)
routers.register('Mascota',views.MascotaList)
routers.register('Paseador',views.PaseadorList)

urlpatterns = [
    path('',include(routers.urls))
]

