from django.db import models

# Create your models here.
class Curso(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    detalle = models.TextField()

    def __str__(self):
        return self.nombre
    