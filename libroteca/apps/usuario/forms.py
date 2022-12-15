from django import forms


class LoginForm(forms.Form):
    class Meta:
        fields = ('usuario', 'clave')


class RegistroForm(forms.Form):
    class Meta:
        fields = ('usuario', 'clave')
