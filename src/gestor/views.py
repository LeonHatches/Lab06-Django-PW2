from django.shortcuts import render, redirect
from .forms import AlumnoForm
from .models import Alumno

def crear_alumno(request):
    if request.method == 'POST':
        form = AlumnoForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('lista_alumno')
    else:
        form = AlumnoForm()
    
    return render(request, 'gestor/crear_alumno.html', {'form':form})

def lista_alumnos(request):
    alumnos = Alumno.objects.all()
    return render(request, 'gestor/lista_alumnos.html', {'alumnos': alumnos})        