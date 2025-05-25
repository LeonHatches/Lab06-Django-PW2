from django.urls import path
from . import views

urlpatterns = [
    path('subirNotas/', views.subir_notas, name='subir_notas'),
    path('listaNotas/', views.lista_notas, name='lista_notas'),
    path('crearCurso/', views.agregar_curso, name="agregar_curso"),
    path('listaCursos/', views.lista_cursos, name="lista_cursos"),
    path('crearAlumno/', views.crear_alumno, name='crear_alumno'),
    path('listaAlumnos/', views.lista_alumnos, name='lista_alumnos'),
    path('', views.index, name='index'),
]