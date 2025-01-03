from django.db import models
from app2.models import Curso

# Create your models here.
class Estudiante(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    def __str__(self):
        return f"Nombre: {self.nombre} - Curso: {self.curso.nombre}"
    