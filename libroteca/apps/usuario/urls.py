from django.urls import path,include
from django.contrib.auth.views import LoginView

from . import views 


urlpatterns=[
    path("accounts/", include("django.contrib.auth.urls")),
    path('login/', LoginView.as_view(template_name='usuario/login.html'), name="login"),
    path('registro', views.RegistroView.as_view(), name='registro'),
]