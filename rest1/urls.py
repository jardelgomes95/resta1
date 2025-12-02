from .views import home # Importe sua view
from django.urls import path


urlpatterns = [
    path('', home, name='home'),     # A rota raiz (vazia) aponta para nossa view
]