from django.db import models

from apps.libros.models import Libro

class Clasificacion(models.Model):
    genero = models.CharField(max_length=255)

    def __str__(self):
        return self.genero


class ClasificacionDeLibro(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    clasificacion = models.ForeignKey(Clasificacion, on_delete=models.CASCADE)

    def __str__(self):
        """Esta funcion me ayuda a visualizar el título del libro en el administrador de Django"""
        return self.libro.titulo