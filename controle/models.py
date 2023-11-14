from django.db import models
from django.contrib.auth.models import User
from unidades.models import Unidade


MES_CHOICES = (
    ("1", "Janeiro"),
    ("2", "Fevereiro"),
    ("3", "Março"),
    ("4", "Abril"),
    ("5", "Maio"),
    ("6", "Junho"),
    ("7", "Julho"),
    ("8", "Agosto"),
    ("9", "Setembro"),
    ("10", "Outubro"),
    ("11", "Novembro"),
    ("12", "Dezembro"),
)


class ControleTeste(models.Model):
    unidade = models.ForeignKey(Unidade, on_delete=models.SET_NULL, null=True, blank=True)
    responsavel = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    t1hiv_cegonha = models.IntegerField()
    t1hiv_rotina = models.IntegerField()
    t1hiv_mobilizacao = models.IntegerField()
    t1hiv_upa = models.IntegerField()
    t1hiv_pep = models.IntegerField()
    t1hiv_laboratorio = models.IntegerField()
    t1hiv_total_realizado = models.IntegerField()
    t1hiv_invalido = models.IntegerField()
    t1hiv_perdido = models.IntegerField()
    t1hiv_total_reagentes = models.IntegerField()
    t1hiv_testes_estoque = models.IntegerField()
    t1hiv_caixas_solicitadas = models.IntegerField()

    t2hiv_cegonha = models.IntegerField()
    t2hiv_rotina = models.IntegerField()
    t2hiv_mobilizacao = models.IntegerField()
    t2hiv_upa = models.IntegerField()
    t2hiv_pep = models.IntegerField()
    t2hiv_laboratorio = models.IntegerField()
    t2hiv_total_realizado = models.IntegerField()
    t2hiv_invalido = models.IntegerField()
    t2hiv_perdido = models.IntegerField()
    t2hiv_total_reagentes = models.IntegerField()
    t2hiv_testes_estoque = models.IntegerField()
    t2hiv_caixas_solicitadas = models.IntegerField()

    sifilis_cegonha = models.IntegerField()
    sifilis_rotina = models.IntegerField()
    sifilis_mobilizacao = models.IntegerField()
    sifilis_upa = models.IntegerField()
    sifilis_pep = models.IntegerField()
    sifilis_laboratorio = models.IntegerField()
    sifilis_total_realizado = models.IntegerField()
    sifilis_invalido = models.IntegerField()
    sifilis_perdido = models.IntegerField()
    sifilis_total_reagentes = models.IntegerField()
    sifilis_testes_estoque = models.IntegerField()
    sifilis_caixas_solicitadas = models.IntegerField()

    hepatiteb_cegonha = models.IntegerField()
    hepatiteb_rotina = models.IntegerField()
    hepatiteb_mobilizacao = models.IntegerField()
    hepatiteb_upa = models.IntegerField()
    hepatiteb_pep = models.IntegerField()
    hepatiteb_laboratorio = models.IntegerField()
    hepatiteb_total_realizado = models.IntegerField()
    hepatiteb_invalido = models.IntegerField()
    hepatiteb_perdido = models.IntegerField()
    hepatiteb_total_reagentes = models.IntegerField()
    hepatiteb_testes_estoque = models.IntegerField()
    hepatiteb_caixas_solicitadas = models.IntegerField()

    hepatitec_cegonha = models.IntegerField()
    hepatitec_rotina = models.IntegerField()
    hepatitec_mobilizacao = models.IntegerField()
    hepatitec_upa = models.IntegerField()
    hepatitec_pep = models.IntegerField()
    hepatitec_laboratorio = models.IntegerField()
    hepatitec_total_realizado = models.IntegerField()
    hepatitec_invalido = models.IntegerField()
    hepatitec_perdido = models.IntegerField()
    hepatitec_total_reagentes = models.IntegerField()
    hepatitec_testes_estoque = models.IntegerField()
    hepatitec_caixas_solicitadas = models.IntegerField()

    auto_teste_hiv = models.IntegerField()
    auto_teste_hiv_estoque = models.IntegerField()
    auto_teste_hiv_solicitadas = models.IntegerField()

    telefone = models.CharField(max_length=15)
    mes = models.CharField(max_length=3, choices=MES_CHOICES, blank=False, null=False)
    ano = models.CharField(max_length=4)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='testerealizado_created_by')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='testerealizado_updated_by')

    class Meta:
        verbose_name = 'Controle de Teste'
        verbose_name_plural = 'Controle de Testes'

    def __str__(self):
        return str(f"Mês: {self.mes} - Unidade: {self.unidade.apelido}")
