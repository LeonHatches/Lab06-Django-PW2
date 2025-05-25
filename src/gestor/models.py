from django.db import models

class Alumno(models.Model):
    CUI       = models.CharField(max_length=8, unique=True)
    nombres   = models.CharField(max_length=200)
    apellidos = models.CharField(max_length=200)

    def __str__(self):
        return self.CUI