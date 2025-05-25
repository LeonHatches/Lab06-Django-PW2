from django.shortcuts import render, redirect

from .forms import AlumnoForm, CursoForm, NotaForm
from .models import Alumno, Curso, NotaAlumnoPorCurso

def agregar_curso(request):
    if request.method == "POST":
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_cursos')
    else:
        form = CursoForm()
    return render(request, "agregar_curso.html", {"form": form})

def lista_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'lista_cursos.html', {"cursos": cursos})


def crear_alumno(request):
    if request.method == 'POST':
        form = AlumnoForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('lista_alumnos')
    else:
        form = AlumnoForm()
    
    return render(request, 'gestor/crear_alumno.html', {'form':form})

def lista_alumnos(request):
    alumnos = Alumno.objects.all()
    return render(request, 'gestor/lista_alumnos.html', {'alumnos': alumnos})        

def subir_notas(request):
    if request.method == 'POST':
        form = NotaForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('lista_notas')
    else:
        form = NotaForm()

    return render(request, 'gestor/subir_notas.html', {'form':form})

def lista_notas(request):
    notas = NotaAlumnoPorCurso.objects.all()
    return render(request, 'gestor/lista_notas.html', {'notas':notas})