from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def bienvenida(request):
    return HttpResponse("Hola Usuarios Art Sena, BIENVENIDOS ...")


def inicio(request):
    return render(request, "home/index.html")

def artistas(request):
    return render(request, 'artistas/artistas.html')


def obras(request):
    return render(request, 'obras/obras.html')


def detalle_obra(request):
    return render(request, 'obras/detalle_obra.html')