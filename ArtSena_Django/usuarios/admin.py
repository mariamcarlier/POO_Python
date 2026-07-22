from django.contrib import admin

from .models import ObraArte

#admin.site.register(ObraArte) forma de regitro simple

@admin.register(ObraArte)  # forma de registro con decorador
class ObraArteAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'fecha_creacion', 'precio')  # Campos que se mostrarán en la lista de administración
    search_fields = ('titulo', 'autor')  # Campos por los que se puede buscar
    list_filter = ('fecha_creacion',)  # Filtros para la lista de administración
    ordering = ('-fecha_creacion',)  # Ordenamiento por defecto
    


# Register your models here.
