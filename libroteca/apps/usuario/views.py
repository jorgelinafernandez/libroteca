from django.shortcuts import render

from django.views import View

from apps.usuario.forms import RegistroForm

class RegistroView(View):
    form_class = RegistroForm
    template_name = 'usuario/registro.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'formulario': form})
