from django.db import models

# Create your models here.

class analisis_De_Riesgo(models.Model):
    nombre = models.CharField(max_length=40)
    Operacion = models.CharField(max_length=40)
    numero = models.IntegerField()

class permiso_de_trabajo(models.Model):
    nombre = models.CharField(max_length=40)
    Operacion = models.CharField(max_length=40)
    numero =  models.IntegerField()


class trabajo_altura(models.Model):
    nombre = models.CharField(max_length=40)
    Operacion = models.CharField(max_length=40)
    numero =  models.IntegerField()