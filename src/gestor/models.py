from django.db import models

class Alumno(models.Model):
    CUI       = models.CharField(max_length=8, unique=True)
    nombres   = models.CharField(max_length=200)
    apellidos = models.CharField(max_length=200)

    def __str__(self):
        return self.CUI

class Curso(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    codigo = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f"{self.nombre} ({self.codigo})"
    
class NotaAlumnoPorCurso(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    nota = models.DecimalField(max_digits=2, decimal_places=0)

    class Meta:
        unique_together = ('alumno', 'curso')