from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import ObraArte #---🖼️parte/apartado de obras🖼️---

# Create your views here.
def bienvenida(request):
    return HttpResponse("Hola Usuarios Art Sena, BIENVENIDOS ...")


def inicio(request):
    return render(request, "home/index.html")

def artistas(request):
    return render(request, 'artistas/artistas.html')

#---🖼️parte/apartado de obras🖼️---
def obras(request):
    # Obtener todas las obras de la base de datos
    obras_list = ObraArte.objects.all().order_by('-fecha_registro')
    
    # (Opcional) Filtrar por técnica si viene en la URL
    tecnica = request.GET.get('tecnica')
    if tecnica:
        obras_list = obras_list.filter(tecnica__iexact=tecnica)  # filtro insensible a mayúsculas
    
    # Crear el diccionario de context
    context = {
        'obras': obras_list,
        'tecnica_activa': tecnica,  # para resaltar el filtro activo
    }
    
    # Renderizar la plantilla pasando el context
    return render(request, 'obras/obras.html', context)#se agrego el context

def detalle_obra(request, pk):
    # Obtener la obra con el id (pk) o devolver 404 si no existe
    obra = get_object_or_404(ObraArte, pk=pk)
    
    context = {
        'obra': obra,
    }
    return render(request, 'obras/detalle_obra.html', context)


def detalle_obra(request, pk): #como parametro se agrego pk
    # Obtener una sola obra o lanzar error 404
    obra = get_object_or_404(ObraArte, pk=pk)
    context = {
        'obra': obra,
    }
    return render(request, 'obras/detalle_obra.html', context)