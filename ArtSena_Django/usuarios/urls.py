from django.urls import path
from . import views

urlpatterns = [
 path ('bienvenida/', views.bienvenida, name='bienvenida_BASICA'),

 path('', views.inicio, name="inicio"),

 path('artistas/', views.artistas, name="artistas"),

 path('obras/', views.obras, name="obras"),

 path('obra/', views.detalle_obra, name="detalle_obra"),

]