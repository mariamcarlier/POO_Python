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

class Artista(Usuario):
    estilo_artistico = models.CharField(max_length=100)

    def __str__(self):
        return f"Artista: {self.nombre} - {self.estilo_artistico}"

class Cliente(Usuario):
    preferencias_arte = models.CharField(max_length=150, blank=True, null=True)
    direccion = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"Cliente: {self.nombre}"
    
class AdministradorGaleria(Usuario):
    rol_interno = models.CharField(max_length=50, default="Curador")

    def __str__(self):
        return f"Admin: {self.nombre} ({self.rol_interno})"


class ObraArte(models.Model):
    ESTADOS_VALIDOS = [
    ('Disponible', 'Disponible'),
    ('Reservada', 'Reservada'),
    ('Vendida', 'Vendida'),
    ]

    id_obra = models.AutoField(primary_key=True)       # Columna: id_obra (Clave Primaria)
    titulo = models.CharField(max_length=150)          # Columna: titulo
    tecnica = models.CharField(max_length=100)         # Columna: tecnica
    anio = models.IntegerField(null=True, blank=True)                       # Columna: anio
    dimensiones = models.CharField(max_length=50, null=True, blank=True)      # Columna: dimensiones
    precio = models.DecimalField(max_digits=12, decimal_places=2) # Columna: precio (_precio protegido)
    disponibilidad = models.CharField(
        max_length=20, 
        choices=ESTADOS_VALIDOS, 
        default='Disponible'
    )                                                  # Columna: disponibilidad
    
    fecha_registro = models.DateField(auto_now_add=True) # Columna: fecha_registro (Automática)

    # RELACIÓN (Llave Foránea): Una obra es subida por un Artista (Autor)
    # Crea la columna en BD: artista_id (conectada a usuarios_artista)
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE, related_name='obras', null=True, blank=True)

    def __str__(self):
        if self.artista:
            return f"'{self.titulo}' por {self.artista.nombre} ({self.disponibilidad})"
        else:
            return f"'{self.titulo}' (sin artista) ({self.disponibilidad})"   