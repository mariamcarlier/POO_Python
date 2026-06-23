from unittest import loader

from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader  


# Create your views here.
def saludar(request):
    template = loader.get_template('saludar.html')
    return HttpResponse(template.render())
