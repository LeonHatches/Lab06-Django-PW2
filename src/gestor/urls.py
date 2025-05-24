from django.urls import path
from . import views

urlpatterns = [
    path("agregar_curso", views.agregar_curso, name="agregar_curso"),
    path('lista_cursos', views.lista_cursos, name="lista_cursos")
]