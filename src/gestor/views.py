from django.shortcuts import render, redirect

from .forms import CursoForm
from .models import Curso

def agregar_curso(request):
    if request.method == "POST":
        form = CursoForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('lista_cursos')
    else:
        form = CursoForm()
    return render(request, "agregar_curso.html", {"form": form})