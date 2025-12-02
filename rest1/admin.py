from django.contrib import admin
from .models import Participante


# Configura como a tabela aparece para o Admin

@admin.register(Participante)
class ParticipanteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'data_envio')  # Colunas que aparecem na lista
    search_fields = ('nome',)  # C
