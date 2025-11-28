from django.shortcuts import render
from django.contrib import messages
from .models import Participante


def home(request):
    if request.method == "POST":
        nome_recebido = request.POST.get('nome_usuario')

        # Validação simples: não salvar se estiver vazio
        if nome_recebido:
            Participante.objects.create(nome=nome_recebido)
            messages.success(request, 'Nome salvo com sucesso!')
        else:
            messages.error(request, 'Por favor, digite um nome.')

    return render(request, 'index.html')