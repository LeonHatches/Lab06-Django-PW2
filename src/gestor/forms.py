from django import forms
from .models import Curso

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ["nombre", "codigo"]

    def clean_nombre(self):
        nombre = self.cleaned_data.get("nombre")
        if Curso.objects.filter(nombre=nombre).exists():
            raise forms.ValidationError("Ya existe un curso con este nombre.")
        return nombre

    def clean_codigo(self):
        codigo = self.cleaned_data.get("codigo")
        if Curso.objects.filter(codigo=codigo).exists():
            raise forms.ValidationError("Código ya registrado")
        return codigo
