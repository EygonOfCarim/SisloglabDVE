from django.db import models
from django.contrib.auth.models import User


class Unidade(models.Model):
    cnes = models.CharField(unique=True)
    razao_social = models.CharField(max_length=150, unique=True)
    apelido = models.CharField(max_length=100)
    cep = models.CharField(max_length=9)
    endereco = models.CharField(max_length=100)
    numero = models.IntegerField()
    bairro = models.CharField(max_length=50)
    uf = models.CharField(max_length=2)
    municipio = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)
    rt = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='unidade_created_by')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='unidade_updated_by')

    class Meta:
        verbose_name = 'Unidade'
        verbose_name_plural = 'Unidades'

    def __str__(self):
        return str(self.apelido)

