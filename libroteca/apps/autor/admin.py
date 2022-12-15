from django.contrib import admin

from apps.autor.models import Autor


@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'nacimiento')
    search_fields = ('nombre', 'apellido')
    list_filter = ('nacimiento',)