from django.db import models

# Create your models here.
class Usuario(models.Model):

    id_usuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20)
    contraseña = models.CharField(max_length=255)

    class Meta:
        abstract = True