from django.contrib import admin

from apps.resenias.models import Resenia


@admin.register(Resenia)
class ReseniaAdmin(admin.ModelAdmin):
    list_display = ('descripcion', 'calificacion', 'libro')
    search_fields = ('descripcion', 'calificacion')
    list_filter = ('descripcion', 'calificacion', 'libro')