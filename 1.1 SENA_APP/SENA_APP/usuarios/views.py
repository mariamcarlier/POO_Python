from unittest import loader

from django.http import HttpResponse
from django.shortcuts import render #renderiza paginas web
from django.template import context, loader  

from .models import Usuario

# Create your views here.
def saludar(request):
    template = loader.get_template('saludar.html')
    return HttpResponse(template.render())

# creando una funcion nueva para conectar el template , cargar los datos =  QuerySets y importando .models
#relacion usuario servidor
def usuarios (request):
    template = loader.get_template('usuarios.html')
    usuarios = Usuario.objects.all() .values() # select * from usuarios_

        #referenciar los datos del backend con el fronted - Crear un Context = CONTEXTO
    context=  {
        'usuarios_html': usuarios
    }    
        # hacer la referencia al templete con los datos y devolver el resultado de la funcion y dar como respuesta el request(solicitud del navegador) 
        # pasa de vista funcion , trajo los datos del modelo y (contexto para enviarlo al fronted) se creo el template 

    return HttpResponse(template.render(context, request))
        #crear la url y hacer la vista
        