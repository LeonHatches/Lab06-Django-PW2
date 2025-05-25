from django.urls import path
from . import views

urlspatterns = [
    path('alumno/crear/', views.crear_alumno, name='crear_alumno'),
    path('alumno/lista/', views.lista_alumnos, name='lista_alumnos'),
]