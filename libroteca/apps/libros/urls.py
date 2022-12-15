from django.urls import path
from django.contrib.auth.decorators import login_required


from .views import (
    HomeListView,
    BuscarLibroListView,
    BuscarLibrosNuevosListView,
    LibrosTopCalificadosListView,
    LibroDetailView,
    LibroPorCategoriaListView
)


urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('libros/buscar', BuscarLibroListView.as_view(), name='buscar_libro'),
    path('libro/<pk>', LibroDetailView.as_view(), name='detalle_libro'),
    path('libros/nuevos', BuscarLibrosNuevosListView.as_view(), name='filtro_libro_nuevos'),
    path('libros/filtro_categoria/<id>', LibroPorCategoriaListView.as_view(), name='filtro_libro_categoria'),
    path('libros/top-10', login_required(LibrosTopCalificadosListView.as_view()), name='filtro_top_10'),
]