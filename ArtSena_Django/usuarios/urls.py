from django.urls import path
from . import views

urlpatterns = [
 path('saludar/', views.saludar, name='saludo'),
]