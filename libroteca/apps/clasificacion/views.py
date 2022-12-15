from django.views.generic import ListView

from apps.clasificacion.models import Clasificacion


class FiltrarLibroPorCategoriaListView(ListView):
    """Seleccionar categoria para filtrar libros."""
    model = Clasificacion 
    context_object_name = 'categorias'
    template_name = 'clasificacion/filtrar_por_categoria.html'
    ordering = ['id']
