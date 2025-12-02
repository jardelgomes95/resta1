from django.db import models

class Participante(models.Model):
    nome = models.CharField(max_length=200, verbose_name="Nome da Pessoa")
    data_envio = models.DateTimeField(auto_now_add=True, verbose_name="Enviado em")

    def __str__(self):
        return self.nome