from django import forms
from .models import Alumno

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ['CUI', 'nombres', 'apellidos']
    
    def clean_CUI(self):
        CUI = self.cleaned_data.get('CUI')
        if Alumno.objects.filter(CUI=CUI).exists():
            raise forms.ValidationError("El CUI ingresado ya EXISTE.")
        return CUI