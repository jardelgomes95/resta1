from django.contrib import admin
from .models import Participante

from django.views.decorators.csrf import csrf_exempt


# Configura como a tabela aparece para o Admin
@csrf_exempt
@admin.register(Participante)
class ParticipanteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'data_envio')  # Colunas que aparecem na lista
    search_fields = ('nome',)  # C
