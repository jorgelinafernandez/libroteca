from django.db import models

from apps.autor.models import Autor


class Libro(models.Model):
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    cantidad_paginas = models.SmallIntegerField()
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    fecha = models.DateField()
    gratuito = models.BooleanField()
    link = models.CharField(max_length=255)

    def __str__(self):
        """Esta funcion me ayuda a visualizar el título del libro en el administrador de Django"""
        return self.titulo