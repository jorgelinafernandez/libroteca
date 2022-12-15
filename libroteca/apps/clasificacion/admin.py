from django.contrib import admin

from apps.clasificacion.models import Clasificacion, ClasificacionDeLibro


@admin.register(Clasificacion)
class ClasificacionAdmin(admin.ModelAdmin):
    list_display = ('genero',)
    search_fields = ('genero',)
    list_filter = ('genero',)


@admin.register(ClasificacionDeLibro)
class ClasificacionDeLibroAdmin(admin.ModelAdmin):
    list_display = ('clasificacion', 'libro')
    list_filter = ('clasificacion', 'libro')