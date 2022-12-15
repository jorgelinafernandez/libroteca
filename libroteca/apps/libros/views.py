from django.views.generic import ListView, DetailView
from django.db.models import Avg

from apps.libros.models import Libro


class HomeListView(ListView):
    """
    Página de inicio de la aplicación libros.
    para hacer esta pag usamos el listview de django 
    que es la forma de hacer una pag listando objetos del modelo
    """
    model = Libro 
    context_object_name = 'libros'
    template_name = 'libros/index.html'
    ordering = ['id']


class LibroDetailView(DetailView):
    model = Libro
    template_name = 'libros/detalle_libro.html'
    context_object_name = 'libro'


class BuscarLibroListView(ListView):
    """Página de busqueda de libros."""
    model = Libro 
    context_object_name = 'libros'
    template_name = 'libros/buscar_libro.html'
    ordering = ['id']

    def get_queryset(self):
        """obtenemos el parametro de busqueda para realizar la busqueda ."""
        parametro_de_busqueda = self.request.GET.get('search')
        if parametro_de_busqueda:
            return Libro.objects.filter(
                titulo__icontains=parametro_de_busqueda
            )
        return Libro.objects.all()


class BuscarLibrosNuevosListView(ListView):
    """Página de libros más nuevos primero."""
    model = Libro 
    context_object_name = 'libros'
    template_name = 'libros/nuevos_libros.html'
    ordering = ['-fecha']


class LibroPorCategoriaListView(ListView):
    """Página de libros filtrados por categoria."""
    model = Libro 
    context_object_name = 'libros'
    template_name = 'libros/filtrado_por_categoria.html'
    ordering = ['id']

    def get_queryset(self):
        """Filtrar libros por categoria de la URL."""
        return Libro.objects.filter(
        clasificaciondelibro__clasificacion__id=self.request.resolver_match.kwargs['id']
    )


class LibrosTopCalificadosListView(ListView):
    """Página de libros filtrados por los gustos del usuario."""
    model = Libro 
    context_object_name = 'libros'
    template_name = 'libros/top_10_mejor_calificado.html'
    # Ordenamos los libros por la calificación de la reseña de mayor a menor
    ordering = ['-resenia__calificacion']
    # Paginación de 10 libros por página, perso solo utilizamos la primera página
    paginate_by = 10

    def get_queryset(self):
        """
            Sobreescribimos el metodo get_queryset para darle un ordenamiento por calificacion.

            Hacemos un Avg (promedio) de las calificaciones de las reseñas de cada libro.
            Y luego ordenamos por -avg_calificacion que es el promedio de las calificaciones de las reseñas.
            El - delante de avg_calificacion indica que se ordena de mayor a menor.
            Para evitar duplicados usamos distinct().
        """
        return Libro.objects.all().annotate(
            avg_calificacion=Avg('resenia__calificacion')
        ).order_by('-avg_calificacion').distinct()
