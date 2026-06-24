from django.db import models

# Create your models here.

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    documento = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo_personal = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=100)