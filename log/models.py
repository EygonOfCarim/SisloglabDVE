import json
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Log(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    acao = models.CharField(max_length=20)
    objeto_afetado = models.CharField(max_length=255, blank=True, null=True)
    mensagem = models.CharField(max_length=255, blank=True, null=True)
    dados_antes = models.TextField(blank=True, null=True)
    dados_depois = models.TextField(blank=True, null=True)
    data_hora = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.usuario.username} - {self.acao} em {self.data_hora}'

    def save(self, *args, **kwargs):
        # Converta objetos datetime para strings antes de salvar
        if self.data_hora:
            self.data_hora = self.data_hora.strftime('%Y-%m-%d %H:%M:%S')

        if self.dados_antes:
            self.dados_antes = str(self.dados_antes)

        if self.dados_depois:
            self.dados_depois = str(self.dados_depois)

        super().save(*args, **kwargs)
