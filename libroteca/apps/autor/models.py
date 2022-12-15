from django.db import models


class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    nacimiento = models.DateField()

    def __str__(self):
        """Esta funcion me ayuda a visualizar el título del libro en el administrador de Django"""
        return f'{self.nombre} {self.apellido}'