from django.urls import path
from django.contrib.auth.decorators import login_required


from .views import (
    ReseniaCreateView,
    ReseniaListView,
)

urlpatterns = [
    path('libro/<id_libro>/crear', login_required(ReseniaCreateView.as_view()), name='crear_resenia'),
    path('libro/<id_libro>', ReseniaListView.as_view(), name='listado_resenias'),
]
