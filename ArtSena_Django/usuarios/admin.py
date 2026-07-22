from django.contrib import admin
from .models import ObraArte

# --- Registro simple (sin personalización) ---
# admin.site.register(ObraArte)  # forma de registro simple

# --- Registro con personalización (decorador) ---
@admin.register(ObraArte)  # forma de registro con decorador
class AdminObras(admin.ModelAdmin):
    # Campos que se mostrarán en la lista de administración
    list_display = ('titulo', 'artista', 'fecha_registro', 'precio', 'disponibilidad')
    
    # Campos por los que se puede buscar
    search_fields = ('titulo', 'artista__nombre', 'tecnica')  # artista__nombre para buscar por nombre del artista
    
    # Filtros para la lista de administración
    list_filter = ('disponibilidad', 'tecnica', 'anio')
    
    # Ordenamiento por defecto (los más recientes primero)
    ordering = ('-fecha_registro',)
    
    # Campos de solo lectura (no se pueden editar)
    readonly_fields = ('fecha_registro',)