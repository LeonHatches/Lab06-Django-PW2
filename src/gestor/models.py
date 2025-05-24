from django.db import models

class Curso(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    codigo = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f"{self.nombre} ({self.codigo})"