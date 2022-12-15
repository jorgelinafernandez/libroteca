from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView

from apps.resenias.models import Resenia


class ReseniaCreateView(CreateView):
    model = Resenia
    template_name = 'resenias/crear_resenia.html'
    fields = ['descripcion', 'calificacion', 'libro', 'usuario']

    def get_success_url(self):
        """sobreescribimos el metodo get_success_url para que nos redireccione al detalle del libro"""
        return reverse('detalle_libro', args=[str(self.kwargs['id_libro'])])


class ReseniaDetailView(DetailView):
    model = Resenia
    template_name = 'resenias/detalle_resenia.html'
    fields = ['descripcion', 'calificacion', 'libro', 'usuario']

    def get_success_url(self):
        """sobreescribimos el metodo get_success_url para que nos redireccione al detalle del libro"""
        return reverse('detalle_libro', args=[str(self.kwargs['id_libro'])])


class ReseniaDetailView(ListView):
    model = Resenia
    template_name = 'resenias/detalle.html'
    context_object_name = 'resenias'


class ReseniaListView(ListView):
    """Página de inicio de la aplicación libros."""
    model = Resenia 
    context_object_name = 'resenias'
    template_name = 'resenias/listado.html'
    ordering = ['id']

    def get_queryset(self):
        """Filtrar resenias por libro."""
        return Resenia.objects.filter(
            libro__id=self.kwargs['id_libro']
        )
