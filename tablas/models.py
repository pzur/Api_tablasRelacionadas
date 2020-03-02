from django.db import models

# Create your models here.

class Cliente(models.Model):
    idcli = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=150)
    apellido = models.CharField(max_length=150)
    direccion = models.CharField(max_length=200)
    telefono = models.IntegerField(blank=True, null=True)
    correo = models.CharField(unique=True, max_length=200, blank=True, null=True)
    foto =models.ImageField(upload_to="clientes",blank=True)

    def __str__(self):
        return self.nombre


   
class Mascota(models.Model):
    idmas = models.AutoField(primary_key=True)
    Cliente = models.ForeignKey(Cliente,related_name='dueño', on_delete=models.CASCADE, blank=True, null=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    raza = models.CharField(max_length=50, blank=True, null=True)
    edad = models.IntegerField(blank=True, null=True)
    peso = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    sexo = models.CharField(max_length=50, blank=True, null=True)
    tipo_animal = models.CharField(max_length=50, blank=True, null=True)
    foto =models.ImageField(upload_to="mascotas",blank=True)

    

    def __str__(self):
        return self.raza


class Paseador(models.Model):
    idpas = models.AutoField(primary_key=True)
    # idesp = models.ForeignKey(Especialidad, models.DO_NOTHING, db_column='idesp', blank=True, null=True)
    nombre = models.CharField(max_length=150)
    apellido = models.CharField(max_length=150)
    direccion = models.CharField(max_length=200)
    rating=models.IntegerField()
    titulo = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=100, blank=True, null=True)
    foto =models.ImageField(upload_to="paseadores",blank=True)
    
    def __str__(self):
        return self.nombre

    # fecha_ingreso = models.DateTimeField(blank=True, null=True)
    # telefono = models.IntegerField(blank=True, null=True)
    # correo = models.CharField(unique=True, max_length=200, blank=True, null=True)
    # dni = models.IntegerField(blank=True, null=True)
