from .models import ControleTeste
from django.forms import ModelForm
from django import forms


class ControleTesteForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['t1hiv_cegonha'].required = True
        self.fields['t1hiv_rotina'].required = True
        self.fields['t1hiv_mobilizacao'].required = True
        self.fields['t1hiv_upa'].required = True
        self.fields['t1hiv_pep'].required = True
        self.fields['t1hiv_laboratorio'].required = True
        self.fields['t1hiv_total_realizado'].required = True
        self.fields['t1hiv_invalido'].required = True
        self.fields['t1hiv_perdido'].required = True
        self.fields['t1hiv_total_reagentes'].required = True
        self.fields['t1hiv_testes_estoque'].required = True
        self.fields['t1hiv_caixas_solicitadas'].required = True

        self.fields['t2hiv_cegonha'].required = True
        self.fields['t2hiv_rotina'].required = True
        self.fields['t2hiv_mobilizacao'].required = True
        self.fields['t2hiv_upa'].required = True
        self.fields['t2hiv_pep'].required = True
        self.fields['t2hiv_laboratorio'].required = True
        self.fields['t2hiv_total_realizado'].required = True
        self.fields['t2hiv_invalido'].required = True
        self.fields['t2hiv_perdido'].required = True
        self.fields['t2hiv_total_reagentes'].required = True
        self.fields['t2hiv_testes_estoque'].required = True
        self.fields['t2hiv_caixas_solicitadas'].required = True

        self.fields['sifilis_cegonha'].required = True
        self.fields['sifilis_rotina'].required = True
        self.fields['sifilis_mobilizacao'].required = True
        self.fields['sifilis_upa'].required = True
        self.fields['sifilis_pep'].required = True
        self.fields['sifilis_laboratorio'].required = True
        self.fields['sifilis_total_realizado'].required = True
        self.fields['sifilis_invalido'].required = True
        self.fields['sifilis_perdido'].required = True
        self.fields['sifilis_total_reagentes'].required = True
        self.fields['sifilis_testes_estoque'].required = True
        self.fields['sifilis_caixas_solicitadas'].required = True

        self.fields['hepatiteb_cegonha'].required = True
        self.fields['hepatiteb_rotina'].required = True
        self.fields['hepatiteb_mobilizacao'].required = True
        self.fields['hepatiteb_upa'].required = True
        self.fields['hepatiteb_pep'].required = True
        self.fields['hepatiteb_laboratorio'].required = True
        self.fields['hepatiteb_total_realizado'].required = True
        self.fields['hepatiteb_invalido'].required = True
        self.fields['hepatiteb_perdido'].required = True
        self.fields['hepatiteb_total_reagentes'].required = True
        self.fields['hepatiteb_testes_estoque'].required = True
        self.fields['hepatiteb_caixas_solicitadas'].required = True

        self.fields['hepatitec_cegonha'].required = True
        self.fields['hepatitec_rotina'].required = True
        self.fields['hepatitec_mobilizacao'].required = True
        self.fields['hepatitec_upa'].required = True
        self.fields['hepatitec_pep'].required = True
        self.fields['hepatitec_laboratorio'].required = True
        self.fields['hepatitec_total_realizado'].required = True
        self.fields['hepatitec_invalido'].required = True
        self.fields['hepatitec_perdido'].required = True
        self.fields['hepatitec_total_reagentes'].required = True
        self.fields['hepatitec_testes_estoque'].required = True
        self.fields['hepatitec_caixas_solicitadas'].required = True

        self.fields['auto_teste_hiv'].required = True
        self.fields['auto_teste_hiv_estoque'].required = True
        self.fields['auto_teste_hiv_solicitadas'].required = True

        self.fields['telefone'].required = False

    class Meta:
        model = ControleTeste
        fields = [
            't1hiv_cegonha',
            't1hiv_rotina',
            't1hiv_mobilizacao',
            't1hiv_upa',
            't1hiv_pep',
            't1hiv_laboratorio',
            't1hiv_total_realizado',
            't1hiv_invalido',
            't1hiv_perdido',
            't1hiv_total_reagentes',
            't1hiv_testes_estoque',
            't1hiv_caixas_solicitadas',

            't2hiv_cegonha',
            't2hiv_rotina',
            't2hiv_mobilizacao',
            't2hiv_upa',
            't2hiv_pep',
            't2hiv_laboratorio',
            't2hiv_total_realizado',
            't2hiv_invalido',
            't2hiv_perdido',
            't2hiv_total_reagentes',
            't2hiv_testes_estoque',
            't2hiv_caixas_solicitadas',

            'sifilis_cegonha',
            'sifilis_rotina',
            'sifilis_mobilizacao',
            'sifilis_upa',
            'sifilis_pep',
            'sifilis_laboratorio',
            'sifilis_total_realizado',
            'sifilis_invalido',
            'sifilis_perdido',
            'sifilis_total_reagentes',
            'sifilis_testes_estoque',
            'sifilis_caixas_solicitadas',

            'hepatiteb_cegonha',
            'hepatiteb_rotina',
            'hepatiteb_mobilizacao',
            'hepatiteb_upa',
            'hepatiteb_pep',
            'hepatiteb_laboratorio',
            'hepatiteb_total_realizado',
            'hepatiteb_invalido',
            'hepatiteb_perdido',
            'hepatiteb_total_reagentes',
            'hepatiteb_testes_estoque',
            'hepatiteb_caixas_solicitadas',

            'hepatitec_cegonha',
            'hepatitec_rotina',
            'hepatitec_mobilizacao',
            'hepatitec_upa',
            'hepatitec_pep',
            'hepatitec_laboratorio',
            'hepatitec_total_realizado',
            'hepatitec_invalido',
            'hepatitec_perdido',
            'hepatitec_total_reagentes',
            'hepatitec_testes_estoque',
            'hepatitec_caixas_solicitadas',

            'auto_teste_hiv',
            'auto_teste_hiv_estoque',
            'auto_teste_hiv_solicitadas',

            'telefone',
        ]

        widgets = {
            't1hiv_cegonha': forms.NumberInput(attrs={'class': 't1hiv insert form-control text-center', 'type': 'number', 'onclick': 'select()', 'min': '0', 'oninput': 'validity.valid||(value="0");'}),
            't1hiv_rotina': forms.NumberInput(attrs={'class': 't1hiv insert form-control text-center', 'type': 'number', 'onclick': 'select()', 'min': '0', 'oninput': 'validity.valid||(value="0");'}),
            't1hiv_mobilizacao': forms.NumberInput(attrs={'class': 't1hiv insert form-control text-center', 'type': 'number', 'onclick': 'select()', 'min': '0', 'oninput': 'validity.valid||(value="0");'}),
            't1hiv_upa': forms.NumberInput(attrs={'class': 't1hiv insert form-control text-center', 'type': 'number', 'onclick': 'select()', 'min': '0', 'oninput': 'validity.valid||(value="0");'}),
            't1hiv_pep': forms.NumberInput(attrs={'class': 't1hiv insert form-control text-center', 'type': 'number', 'onclick': 'select()', 'min': '0', 'oninput': 'validity.valid||(value="0");'}),
            't1hiv_laboratorio': forms.NumberInput(attrs={'class': 't1hiv insert form-control text-center', 'type': 'number', 'onclick': 'select()', 'min': '0', 'oninput': 'validity.valid||(value="0");'}),
            't1hiv_total_realizado': forms.NumberInput(attrs={'tabindex': '-1', 'class': 'totalt1hiv insert form-control text-center', 'type': 'number', 'onclick': 'select()', 'readonly': 'readonly'}),
            't1hiv_invalido': forms.NumberInput(attrs={'class': 'insert form-control text-center', 'type': 'number', 'onclick': 'select()', 'min': '0', 'oninput': 'validity.valid||(value="0");'}),
            't1hiv_perdido': forms.NumberInput(attrs={'class': 'insert form-control text-center', 'type': 'number', 'onclick': 'select()', 'min': '0', 'oninput': 'validity.valid||(value="0");'}),
            't1hiv_total_reagentes': forms.NumberInput(attrs={'class': 'insert form-control text-center', 'type': 'number', 'onclick': 'select()', 'min': '0', 'oninput': 'validity.valid||(value="0");'}),
            't1hiv_testes_estoque': forms.NumberInput(attrs={'class': 'insert form-control text-center', 'type': 'number', 'onclick': 'select()', 'min': '0', 'oninput': 'validity.valid||(value="0");'}),
            't1hiv_caixas_solicitadas': forms.NumberInput(attrs={'class': 'insert form-control text-center', 'type': 'number', 'onclick': 'select()', 'min': '0', 'oninput': 'validity.valid||(value="0");'}),

            't2hiv_cegonha': forms.NumberInput(attrs={'class': 't2hiv insert form-control text-center', 'type': 'number', 'onclick': 'select()', 'min': '0', 'oninput': 'validity.valid||(value="0");'}),
            't2hiv_rotina': forms.NumberInput(attrs={'class': 't2hiv insert form-control text-center', 'type': 'number', 'onclick': 'select()', 'min': '0', 'oninput': 'validity.valid||(value="0");'}),
            't2hiv_mobilizacao': forms.NumberInput(attrs={'class': 't2hiv insert form-control text-center', 'type': 'number', 'onclick': 'select()', 'min': '0', 'oninput': 'validity.valid||(value="0");'}),
            't2hiv_upa': forms.NumberInput(attrs={'class': 't2hiv insert form-control text-center', 'type': 'number', 'onclick': 'select()', 'min': '0', 'oninput': 'validity.valid||(value="0");'}),
            't2hiv_pep': forms.NumberInput(attrs={'class': 't2hiv insert form-control text-center', 'type': 'number', 'onclick': 'select()', 'min': '0', 'oninput': 'validity.valid||(value="0");'}),
            't2hiv_laboratorio': forms.NumberInput(attrs={'class': 't2hiv insert form-control text-center', 'type': 'number', 'onclick': 'select()', 'min': '0', 'oninput': 'validity.valid||(value="0");'}),
            't2hiv_total_realizado': forms.NumberInput(attrs={'tabindex': '-1', 'class': 'totalt2hiv insert form-control text-center', 'type': 'number', 'onclick': 'select()', 'readonly': 'readonly'}),
            't2hiv_invalido': forms.NumberInput(attrs={'class': 'insert form-control text-center', 'type': 'number', 'onclick': 'select()', 'min': '0', 'oninput': 'validity.valid||(value="0");'}),
            't2hiv_perdido': forms.NumberInput(attrs={'class': 'insert form-control text-center', 'type': 'number', 'onclick': 'select()', 'min': '0', 'oninput': 'validity.valid||(value="0");'}),
            't2hiv_total_reagentes': forms.NumberInput(attrs={'class': 'insert form-control text-center', 'type': 'number', 'onclick': 'select()', 'min': '0', 'oninput': 'validity.valid||(value="0");'}),
            't2hiv_testes_estoque': forms.NumberInput(attrs={'class': 'insert form-control text-center', 'type': 'number', 'onclick': 'select()', 'min': '0', 'oninput': 'validity.valid||(value="0");'}),
            't2hiv_caixas_solicitadas': forms.NumberInput(attrs={'class': 'insert form-control text-center', 'type': 'number', 'onclick': 'select()', 'min': '0', 'oninput': 'validity.valid||(value="0");'}),

            'sifilis_cegonha': forms.NumberInput(attrs={'class': 'sifilis insert form-control text-center', 'type': 'number', 'onclick': 'select()', 'min': '0', 'oninput': 'validity.valid||(value="0");'}),
            'sifilis_rotina': forms.NumberInput(attrs={'class': 'sifilis insert form-control text-center', 'type': 'number', 'onclick': 'select()', 'min': '0', 'oninput': 'validity.valid||(value="0");'}),
            'sifilis_mobilizacao': forms.NumberInput(attrs={'class': 'sifilis insert form-control text-center', 'type': 'number', 'onclick': 'select()', 'min': '0', 'oninput': 'validity.valid||(value="0";'}),
            'sifilis_upa': forms.NumberInput(attrs={'class': 'sifilis insert form-control text-center', 'type': 'number', 'onclick': 'select()', 'min': '0', 'oninput': 'validity.valid||(value="0");'}),
            'sifilis_pep': forms.NumberInput(attrs={'class': 'sifilis insert form-control text-center', 'type': 'number', 'onclick': 'select()', 'min': '0', 'oninput': 'validity.valid||(value="0");'}),
            'sifilis_laboratorio': forms.NumberInput(attrs={'class': 'sifilis insert form-control text-center', 'type': 'number', 'onclick': 'select()', 'min': '0', 'oninput': 'validity.valid||(value="0");'}),
            'sifilis_total_realizado': forms.NumberInput(attrs={'tabindex': '-1', 'class': 'totalsifilis insert form-control text-center', 'type': 'number', 'onclick': 'select()', 'readonly': 'readonly'}),
            'sifilis_invalido': forms.NumberInput(attrs={'class': 'insert form-control text-center', 'type': 'number', 'onclick': 'select()', 'min': '0', 'oninput': 'validity.valid||(value="0");'}),
            'sifilis_perdido': forms.NumberInput(attrs={'class': 'insert form-control text-center', 'type': 'number', 'onclick': 'select()', 'min': '0', 'oninput': 'validity.valid||(value="0");'}),
            'sifilis_total_reagentes': forms.NumberInput(attrs={'class': 'insert form-control text-center', 'type': 'number', 'onclick': 'select()', 'min': '0', 'oninput': 'validity.valid||(value="0");'}),
            'sifilis_testes_estoque': forms.NumberInput(attrs={'class': 'insert form-control text-center', 'type': 'number', 'onclick': 'select()', 'min': '0', 'oninput': 'validity.valid||(value="0");'}),
            'sifilis_caixas_solicitadas': forms.NumberInput(attrs={'class': 'insert form-control text-center', 'type': 'number', 'onclick': 'select()', 'min': '0', 'oninput': 'validity.valid||(value="0");'}),

            'hepatiteb_cegonha': forms.NumberInput(attrs={'class': 'hepatiteb insert form-control text-center', 'type': 'number', 'onclick': 'select()', 'min': '0', 'oninput': 'validity.valid||(value="0");'}),
            'hepatiteb_rotina': forms.NumberInput(attrs={'class': 'hepatiteb insert form-control text-center', 'type': 'number', 'onclick': 'select()', 'min': '0', 'oninput': 'validity.valid||(value="0");'}),
            'hepatiteb_mobilizacao': forms.NumberInput(attrs={'class': 'hepatiteb insert form-control text-center', 'type': 'number', 'onclick': 'select()', 'min': '0', 'oninput': 'validity.valid||(value="0");'}),
            'hepatiteb_upa': forms.NumberInput(attrs={'class': 'hepatiteb insert form-control text-center', 'type': 'number', 'onclick': 'select()', 'min': '0', 'oninput': 'validity.valid||(value="0");'}),
            'hepatiteb_pep': forms.NumberInput(attrs={'class': 'hepatiteb insert form-control text-center', 'type': 'number', 'onclick': 'select()', 'min': '0', 'oninput': 'validity.valid||(value="0");'}),
            'hepatiteb_laboratorio': forms.NumberInput(attrs={'class': 'hepatiteb insert form-control text-center', 'type': 'number', 'onclick': 'select()', 'min': '0', 'oninput': 'validity.valid||(value="0");'}),
            'hepatiteb_total_realizado': forms.NumberInput(attrs={'tabindex': '-1', 'class': 'totalhepatiteb insert form-control text-center', 'type': 'number', 'onclick': 'select()', 'readonly': 'readonly'}),
            'hepatiteb_invalido': forms.NumberInput(attrs={'class': 'insert form-control text-center', 'type': 'number', 'onclick': 'select()', 'min': '0', 'oninput': 'validity.valid||(value="0");'}),
            'hepatiteb_perdido': forms.NumberInput(attrs={'class': 'insert form-control text-center', 'type': 'number', 'onclick': 'select()', 'min': '0', 'oninput': 'validity.valid||(value="0");'}),
            'hepatiteb_total_reagentes': forms.NumberInput(attrs={'class': 'insert form-control text-center', 'type': 'number', 'onclick': 'select()', 'min': '0', 'oninput': 'validity.valid||(value="0");'}),
            'hepatiteb_testes_estoque': forms.NumberInput(attrs={'class': 'insert form-control text-center', 'type': 'number', 'onclick': 'select()', 'min': '0', 'oninput': 'validity.valid||(value="0");'}),
            'hepatiteb_caixas_solicitadas': forms.NumberInput(attrs={'class': 'insert form-control text-center', 'type': 'number', 'onclick': 'select()', 'min': '0', 'oninput': 'validity.valid||(value="0");'}),

            'hepatitec_cegonha': forms.NumberInput(attrs={'class': 'hepatitec insert form-control text-center', 'type': 'number', 'onclick': 'select()', 'min': '0', 'oninput': 'validity.valid||(value="0");'}),
            'hepatitec_rotina': forms.NumberInput(attrs={'class': 'hepatitec insert form-control text-center', 'type': 'number', 'onclick': 'select()', 'min': '0', 'oninput': 'validity.valid||(value="0");'}),
            'hepatitec_mobilizacao': forms.NumberInput(attrs={'class': 'hepatitec insert form-control text-center', 'type': 'number', 'onclick': 'select()', 'min': '0', 'oninput': 'validity.valid||(value="0");'}),
            'hepatitec_upa': forms.NumberInput(attrs={'class': 'hepatitec insert form-control text-center', 'type': 'number', 'onclick': 'select()', 'min': '0', 'oninput': 'validity.valid||(value="0");'}),
            'hepatitec_pep': forms.NumberInput(attrs={'class': 'hepatitec insert form-control text-center', 'type': 'number', 'onclick': 'select()', 'min': '0', 'oninput': 'validity.valid||(value="0");'}),
            'hepatitec_laboratorio': forms.NumberInput(attrs={'class': 'hepatitec insert form-control text-center', 'type': 'number', 'onclick': 'select()', 'min': '0', 'oninput': 'validity.valid||(value="0");'}),
            'hepatitec_total_realizado': forms.NumberInput(attrs={'tabindex': '-1', 'class': 'totalhepatitec insert form-control text-center', 'type': 'number', 'onclick': 'select()', 'readonly': 'readonly'}),
            'hepatitec_invalido': forms.NumberInput(attrs={'class': 'insert form-control text-center', 'type': 'number', 'onclick': 'select()', 'min': '0', 'oninput': 'validity.valid||(value="0");'}),
            'hepatitec_perdido': forms.NumberInput(attrs={'class': 'insert form-control text-center', 'type': 'number', 'onclick': 'select()', 'min': '0', 'oninput': 'validity.valid||(value="0");'}),
            'hepatitec_total_reagentes': forms.NumberInput(attrs={'class': 'insert form-control text-center', 'type': 'number', 'onclick': 'select()', 'min': '0', 'oninput': 'validity.valid||(value="0");'}),
            'hepatitec_testes_estoque': forms.NumberInput(attrs={'class': 'insert form-control text-center', 'type': 'number', 'onclick': 'select()', 'min': '0', 'oninput': 'validity.valid||(value="0");'}),
            'hepatitec_caixas_solicitadas': forms.NumberInput(attrs={'class': 'insert form-control text-center', 'type': 'number', 'onclick': 'select()', 'min': '0', 'oninput': 'validity.valid||(value="0");'}),

            'auto_teste_hiv': forms.NumberInput(attrs={'class': 'insert form-control text-center', 'type': 'number', 'onclick': 'select()', 'min': '0', 'oninput': 'validity.valid||(value="0");'}),
            'auto_teste_hiv_estoque': forms.NumberInput(attrs={'class': 'insert form-control text-center', 'type': 'number', 'onclick': 'select()', 'min': '0', 'oninput': 'validity.valid||(value="0");'}),
            'auto_teste_hiv_solicitadas': forms.NumberInput(attrs={'class': 'insert form-control text-center', 'type': 'number', 'onclick': 'select()', 'min': '0', 'oninput': 'validity.valid||(value="0");'}),

            'telefone': forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'required': ''}),
        }


