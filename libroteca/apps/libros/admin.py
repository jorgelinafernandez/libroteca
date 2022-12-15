from django.contrib import admin

from apps.libros.models import Libro


@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'cantidad_paginas', 'autor', 'fecha', 'gratuito', 'link')
    search_fields = ('titulo', 'cantidad_paginas', 'fecha', 'gratuito', 'link')
    list_filter = ('titulo', 'cantidad_paginas', 'autor', 'fecha', 'gratuito', 'link')