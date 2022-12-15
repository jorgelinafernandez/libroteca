from django.urls import path

from .views import FiltrarLibroPorCategoriaListView


urlpatterns = [
    path('filtrar', FiltrarLibroPorCategoriaListView.as_view(), name='filtrar_libro_categoria'),
]
