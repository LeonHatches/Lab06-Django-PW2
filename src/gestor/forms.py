from django import forms
from .models import Curso, NotaAlumnoPorCurso

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

class NotaForm(forms.ModelForm):
    cui_alumno = forms.CharField(max_length=8, label="CUI")

    class Meta:
        model =  NotaAlumnoPorCurso
        # fields = ["cui_alumno", "curso", "nota"]
        fields = ["curso", "nota"]

    # def clean_cui_alumno(self):
    #     cui = self.cleaned_data.get('cui_alumno')
    #     if not Curso.objects.filter(cui=cui).exists()
    #         raise forms.ValidationError("El alumno con este CUI no existe")
        
    #     return cui