from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now

from apps.libros.models import Libro

class Resenia(models.Model):
    descripcion = models.TextField()
    calificacion = models.SmallIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateTimeField(default=now)

    def __str__(self):
        """Esta funcion me ayuda a visualizar el título del libro en el administrador de Django"""
        return f'Calificación: {self.calificacion} Libro: {self.libro}'