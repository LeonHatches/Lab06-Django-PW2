from django.urls import path
from . import views

urlpatterns = [
    path("agregar_curso", views.agregar_curso, name="agregar_curso"),
    path('lista_cursos', views.lista_cursos, name="lista_cursos"),
    path('crear/', views.crear_alumno, name='crear_alumno'),
    path('lista/', views.lista_alumnos, name='lista_alumnos'),
    path('subir_notas', views.subir_notas, name='subir_notas'),
    path('lista_notas', views.lista_notas, name='lista_notas'),
]