from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import PageNotAnInteger, Paginator, EmptyPage
from django.db import IntegrityError
from django.db.models import IntegerField
from django.db.models.functions import Cast
from django.shortcuts import render, redirect
from django.utils.safestring import mark_safe
from .models import ControleTeste, MES_CHOICES
from unidades.models import Unidade
from django.contrib.auth.models import User
from datetime import datetime
from .forms import ControleTesteForm


@login_required
def criar_controle(request):
    if request.method == "POST":
        unidade = Unidade.objects.get(pk=request.user.userprofile.unidade_id)
        usuario = User.objects.get(pk=request.user.pk)
        formulario = ControleTesteForm(request.POST)
        if request.POST.get("mes") is not None:
            if formulario.is_valid():
                try:
                    ControleTeste.objects.create(
                        unidade=unidade,
                        t1hiv_cegonha=request.POST.get('t1hiv_cegonha'),
                        t1hiv_rotina=request.POST.get('t1hiv_rotina'),
                        t1hiv_mobilizacao=request.POST.get('t1hiv_mobilizacao'),
                        t1hiv_upa=request.POST.get('t1hiv_upa'),
                        t1hiv_pep=request.POST.get('t1hiv_pep'),
                        t1hiv_laboratorio=request.POST.get('t1hiv_laboratorio'),
                        t1hiv_total_realizado=request.POST.get('t1hiv_total_realizado'),
                        t1hiv_invalido=request.POST.get('t1hiv_invalido'),
                        t1hiv_perdido=request.POST.get('t1hiv_perdido'),
                        t1hiv_total_reagentes=request.POST.get('t1hiv_total_reagentes'),
                        t1hiv_testes_estoque=request.POST.get('t1hiv_testes_estoque'),
                        t1hiv_caixas_solicitadas=request.POST.get('t1hiv_caixas_solicitadas'),

                        t2hiv_cegonha=request.POST.get('t2hiv_cegonha'),
                        t2hiv_rotina=request.POST.get('t2hiv_rotina'),
                        t2hiv_mobilizacao=request.POST.get('t2hiv_mobilizacao'),
                        t2hiv_upa=request.POST.get('t2hiv_upa'),
                        t2hiv_pep=request.POST.get('t2hiv_pep'),
                        t2hiv_laboratorio=request.POST.get('t2hiv_laboratorio'),
                        t2hiv_total_realizado=request.POST.get('t2hiv_total_realizado'),
                        t2hiv_invalido=request.POST.get('t2hiv_invalido'),
                        t2hiv_perdido=request.POST.get('t2hiv_perdido'),
                        t2hiv_total_reagentes=request.POST.get('t2hiv_total_reagentes'),
                        t2hiv_testes_estoque=request.POST.get('t2hiv_testes_estoque'),
                        t2hiv_caixas_solicitadas=request.POST.get('t2hiv_caixas_solicitadas'),

                        sifilis_cegonha=request.POST.get('sifilis_cegonha'),
                        sifilis_rotina=request.POST.get('sifilis_rotina'),
                        sifilis_mobilizacao=request.POST.get('sifilis_mobilizacao'),
                        sifilis_upa=request.POST.get('sifilis_upa'),
                        sifilis_pep=request.POST.get('sifilis_pep'),
                        sifilis_laboratorio=request.POST.get('sifilis_laboratorio'),
                        sifilis_total_realizado=request.POST.get('sifilis_total_realizado'),
                        sifilis_invalido=request.POST.get('sifilis_invalido'),
                        sifilis_perdido=request.POST.get('sifilis_perdido'),
                        sifilis_total_reagentes=request.POST.get('sifilis_total_reagentes'),
                        sifilis_testes_estoque=request.POST.get('sifilis_testes_estoque'),
                        sifilis_caixas_solicitadas=request.POST.get('sifilis_caixas_solicitadas'),

                        hepatiteb_cegonha=request.POST.get('hepatiteb_cegonha'),
                        hepatiteb_rotina=request.POST.get('hepatiteb_rotina'),
                        hepatiteb_mobilizacao=request.POST.get('hepatiteb_mobilizacao'),
                        hepatiteb_upa=request.POST.get('hepatiteb_upa'),
                        hepatiteb_pep=request.POST.get('hepatiteb_pep'),
                        hepatiteb_laboratorio=request.POST.get('hepatiteb_laboratorio'),
                        hepatiteb_total_realizado=request.POST.get('hepatiteb_total_realizado'),
                        hepatiteb_invalido=request.POST.get('hepatiteb_invalido'),
                        hepatiteb_perdido=request.POST.get('hepatiteb_perdido'),
                        hepatiteb_total_reagentes=request.POST.get('hepatiteb_total_reagentes'),
                        hepatiteb_testes_estoque=request.POST.get('hepatiteb_testes_estoque'),
                        hepatiteb_caixas_solicitadas=request.POST.get('hepatiteb_caixas_solicitadas'),

                        hepatitec_cegonha=request.POST.get('hepatitec_cegonha'),
                        hepatitec_rotina=request.POST.get('hepatitec_rotina'),
                        hepatitec_mobilizacao=request.POST.get('hepatitec_mobilizacao'),
                        hepatitec_upa=request.POST.get('hepatitec_upa'),
                        hepatitec_pep=request.POST.get('hepatitec_pep'),
                        hepatitec_laboratorio=request.POST.get('hepatitec_laboratorio'),
                        hepatitec_total_realizado=request.POST.get('hepatitec_total_realizado'),
                        hepatitec_invalido=request.POST.get('hepatitec_invalido'),
                        hepatitec_perdido=request.POST.get('hepatitec_perdido'),
                        hepatitec_total_reagentes=request.POST.get('hepatitec_total_reagentes'),
                        hepatitec_testes_estoque=request.POST.get('hepatitec_testes_estoque'),
                        hepatitec_caixas_solicitadas=request.POST.get('hepatitec_caixas_solicitadas'),

                        auto_teste_hiv=request.POST.get('auto_teste_hiv'),
                        auto_teste_hiv_estoque=request.POST.get('auto_teste_hiv_estoque'),
                        auto_teste_hiv_solicitadas=request.POST.get('auto_teste_hiv_solicitadas'),

                        telefone=request.POST.get('telefone'),
                        mes=request.POST.get('mes'),
                        ano=request.POST.get('ano'),
                        responsavel=usuario,
                        created_by=usuario,
                        updated_by=usuario,
                    )
                    messages.add_message(request=request, message='Cadastrado com sucesso!',
                                         level=messages.SUCCESS)
                    return redirect('controles')
                except IntegrityError:
                    messages.add_message(request=request, message=mark_safe(
                        f'Ocorreu um erro na gravação dos dados! Algum valor nulo foi recebido!'),
                                         level=messages.ERROR)
                    unidade = Unidade.objects.get(pk=request.user.userprofile.unidade_id)
                    mes = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
                    meses = []
                    ano = datetime.now().year
                    meses_cadastrados = ControleTeste.objects.filter(unidade=unidade, mes__in=mes, ano=ano)
                    for controle in meses_cadastrados:
                        meses.append(controle.mes)
                    context = {
                        'meses': meses,
                        'escolhas_meses': MES_CHOICES,
                        'form': ControleTesteForm(instance=formulario),
                    }
                    return render(request, 'controle/criar_controle.html', context)
                except Exception as ex:
                    messages.add_message(request=request, message=mark_safe(
                        f'Ocorreu um erro não especificado! Entre em contato e informe a mensagem abaixo. <br> {ex} '),
                                         level=messages.ERROR)
                    return redirect('criar_controle')
            else:
                messages.add_message(request=request,
                                     message='Ocorreu um erro ao validar os dados inseridos! Verifique e tente novamente!',
                                     level=messages.ERROR)
                unidade = Unidade.objects.get(pk=request.user.userprofile.unidade_id)
                mes = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
                meses = []
                ano = datetime.now().year
                meses_cadastrados = ControleTeste.objects.filter(unidade=unidade, mes__in=mes, ano=ano)
                for controle in meses_cadastrados:
                    meses.append(controle.mes)
                context = {
                    'meses': meses,
                    'escolhas_meses': MES_CHOICES,
                    'form': ControleTesteForm(instance=formulario),
                }
                return render(request, 'controle/criar_controle.html', context)
        else:
            messages.add_message(request=request,
                                 message='Selecione um mês!',
                                 level=messages.ERROR)
            mes = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
            mes_atual = datetime.now().month
            meses = []
            ano = datetime.now().year
            meses_cadastrados = ControleTeste.objects.filter(unidade=unidade, mes__in=mes, ano=ano)
            for controle in meses_cadastrados:
                meses.append(controle.mes)
            context = {
                'mes': mes_atual,
                'meses': meses,
                'escolhas_meses': MES_CHOICES,
                'form': formulario,
            }
            return render(request, 'controle/criar_controle.html', context)
    else:
        unidade = Unidade.objects.get(pk=request.user.userprofile.unidade_id)
        mes = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
        mes_atual = datetime.now().month
        meses = []
        ano = datetime.now().year
        meses_cadastrados = ControleTeste.objects.filter(unidade=unidade, mes__in=mes, ano=ano)
        for controle in meses_cadastrados:
            meses.append(controle.mes)
        context = {
            'mes': mes_atual,
            'meses': meses,
            'escolhas_meses': MES_CHOICES,
            'form': ControleTesteForm(),
        }
        return render(request, 'controle/criar_controle.html', context)


@login_required
def editar_controle(request, pk):
    registro = ControleTeste.objects.get(pk=pk)
    unidade = Unidade.objects.get(pk=request.user.userprofile.unidade_id)
    mes = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
    meses = []
    ano = datetime.now().year
    meses_cadastrados = ControleTeste.objects.filter(unidade=unidade, mes__in=mes, ano=ano)
    for controle in meses_cadastrados:
        meses.append(controle.mes)

    if request.method == "POST":
        registro = ControleTeste.objects.get(pk=pk)
        formulario = ControleTesteForm(request.POST, instance=registro)
        if formulario.is_valid() and formulario.has_changed():
            try:
                formulario.save()
                messages.add_message(request=request, message='Atualizado com sucesso!',
                                     level=messages.SUCCESS)
                return redirect('controles')
            except Exception as ex:
                messages.add_message(request=request, message=mark_safe(
                    f'Ocorreu um erro não especificado! Entre em contato e informe a mensagem abaixo. <br> {ex}'),
                                     level=messages.ERROR)
                context = {
                    'form': formulario,
                    'meses': meses,
                    'escolhas_meses': MES_CHOICES,
                    'controle': registro,
                }
                return render(request, 'controle/editar_controle.html', context)
        elif not formulario.has_changed():
            return redirect('controles')
        else:
            messages.add_message(request=request,
                                 message='Ocorreu um erro ao validar os dados inseridos! Verifique e tente novamente!',
                                 level=messages.ERROR)
            context = {
                'form': formulario,
                'meses': meses,
                'escolhas_meses': MES_CHOICES,
                'controle': registro,
            }
            return render(request, 'controle/editar_controle.html', context)
    else:
        if unidade == registro.unidade:
            context = {
                'form': ControleTesteForm(instance=registro),
                'meses': meses,
                'escolhas_meses': MES_CHOICES,
                'controle': registro,
            }
            return render(request, 'controle/editar_controle.html', context)
        else:
            return redirect('controles')


@login_required
def deletar_controle(request, pk):
    ControleTeste.objects.get(pk=pk).delete()
    messages.add_message(request=request,
                         message='Registro excluído com sucesso!',
                         level=messages.SUCCESS)
    return redirect('controles')


@login_required
def controles(request):
    unidades = Unidade.objects.all()
    meses = []
    anos = []
    if request.user.is_superuser:
        registros = ControleTeste.objects.all().order_by(Cast('mes', IntegerField()), 'unidade')
        for mes in registros:
            if mes.mes not in meses:
                meses.append(mes.mes)
        for ano in registros:
            if ano.ano not in anos:
                anos.append(ano.ano)
    else:
        registros = ControleTeste.objects.filter(unidade__id=request.user.userprofile.unidade.id).order_by(
            Cast('mes', IntegerField()), 'unidade')
        for mes in registros:
            if mes.mes not in meses:
                meses.append(mes.mes)
        for ano in registros:
            if ano.ano not in anos:
                anos.append(ano.ano)
    page = request.GET.get('page', 1)
    paginator = Paginator(registros, 10)
    page_range = paginator.get_elided_page_range(number=page)
    try:
        registros = paginator.page(page)
    except PageNotAnInteger:
        registros = paginator.page(1)
    except EmptyPage:
        registros = paginator.page(paginator.num_pages)
    context = {
        'controles': registros,
        'meses': meses,
        'anos': anos,
        'page_range': page_range,
        'unidades': unidades,
    }
    return render(request, 'controle/listar_controle.html', context)


@login_required
def exportar_controles(request):
    if request.user.is_staff:
        registros = ControleTeste.objects.order_by(Cast('mes', IntegerField()), 'ano').values('ano', 'mes').distinct()
        meses = []
        anos = []
        for registro in registros:
            if registro['mes'] not in meses:
                meses.append(registro['mes'])
            if registro['ano'] not in anos:
                anos.append(registro['ano'])
        page = request.GET.get('page', 1)
        paginator = Paginator(registros, 10)
        page_range = paginator.get_elided_page_range(number=page)
        try:
            registros = paginator.page(page)
        except PageNotAnInteger:
            registros = paginator.page(1)
        except EmptyPage:
            registros = paginator.page(paginator.num_pages)
        context = {
            'controles': registros,
            'page_range': page_range,
            'escolhas_meses': MES_CHOICES,
            'anos': anos,
            'meses': meses,
        }
        return render(request, 'controle/exportar_controle.html', context)
    else:
        return redirect('controles')


@login_required
def ver_controle(request, ano, mes):
    variaveis_registro = {
        't1hiv_cegonha': 0,
        't1hiv_rotina': 0,
        't1hiv_mobilizacao': 0,
        't1hiv_upa': 0,
        't1hiv_pep': 0,
        't1hiv_laboratorio': 0,
        't1hiv_total_realizado': 0,
        't1hiv_invalido': 0,
        't1hiv_perdido': 0,
        't1hiv_total_reagentes': 0,
        't1hiv_testes_estoque': 0,
        't1hiv_caixas_solicitadas': 0,

        't2hiv_cegonha': 0,
        't2hiv_rotina': 0,
        't2hiv_mobilizacao': 0,
        't2hiv_upa': 0,
        't2hiv_pep': 0,
        't2hiv_laboratorio': 0,
        't2hiv_total_realizado': 0,
        't2hiv_invalido': 0,
        't2hiv_perdido': 0,
        't2hiv_total_reagentes': 0,
        't2hiv_testes_estoque': 0,
        't2hiv_caixas_solicitadas': 0,

        'sifilis_cegonha': 0,
        'sifilis_rotina': 0,
        'sifilis_mobilizacao': 0,
        'sifilis_upa': 0,
        'sifilis_pep': 0,
        'sifilis_laboratorio': 0,
        'sifilis_total_realizado': 0,
        'sifilis_invalido': 0,
        'sifilis_perdido': 0,
        'sifilis_total_reagentes': 0,
        'sifilis_testes_estoque': 0,
        'sifilis_caixas_solicitadas': 0,

        'hepatiteb_cegonha': 0,
        'hepatiteb_rotina': 0,
        'hepatiteb_mobilizacao': 0,
        'hepatiteb_upa': 0,
        'hepatiteb_pep': 0,
        'hepatiteb_laboratorio': 0,
        'hepatiteb_total_realizado': 0,
        'hepatiteb_invalido': 0,
        'hepatiteb_perdido': 0,
        'hepatiteb_total_reagentes': 0,
        'hepatiteb_testes_estoque': 0,
        'hepatiteb_caixas_solicitadas': 0,

        'hepatitec_cegonha': 0,
        'hepatitec_rotina': 0,
        'hepatitec_mobilizacao': 0,
        'hepatitec_upa': 0,
        'hepatitec_pep': 0,
        'hepatitec_laboratorio': 0,
        'hepatitec_total_realizado': 0,
        'hepatitec_invalido': 0,
        'hepatitec_perdido': 0,
        'hepatitec_total_reagentes': 0,
        'hepatitec_testes_estoque': 0,
        'hepatitec_caixas_solicitadas': 0,

        'auto_teste_hiv': 0,
        'auto_teste_hiv_estoque': 0,
        'auto_teste_hiv_solicitadas': 0,
    }
    registros = ControleTeste.objects.filter(ano=ano, mes=mes).order_by('-unidade')
    unidades = []
    n_preenchidas = []
    for registro in registros:
        unidades.append(registro.unidade.apelido)
        variaveis_registro['t1hiv_cegonha'] += registro.t1hiv_cegonha
        variaveis_registro['t1hiv_rotina'] += registro.t1hiv_rotina
        variaveis_registro['t1hiv_mobilizacao'] += registro.t1hiv_mobilizacao
        variaveis_registro['t1hiv_upa'] += registro.t1hiv_upa
        variaveis_registro['t1hiv_pep'] += registro.t1hiv_pep
        variaveis_registro['t1hiv_laboratorio'] += registro.t1hiv_laboratorio
        variaveis_registro['t1hiv_total_realizado'] += registro.t1hiv_total_realizado
        variaveis_registro['t1hiv_invalido'] += registro.t1hiv_invalido
        variaveis_registro['t1hiv_perdido'] += registro.t1hiv_perdido
        variaveis_registro['t1hiv_total_reagentes'] += registro.t1hiv_total_reagentes
        variaveis_registro['t1hiv_testes_estoque'] += registro.t1hiv_testes_estoque
        variaveis_registro['t1hiv_caixas_solicitadas'] += registro.t1hiv_caixas_solicitadas

        variaveis_registro['t2hiv_cegonha'] += registro.t2hiv_cegonha
        variaveis_registro['t2hiv_rotina'] += registro.t2hiv_rotina
        variaveis_registro['t2hiv_mobilizacao'] += registro.t2hiv_mobilizacao
        variaveis_registro['t2hiv_upa'] += registro.t2hiv_upa
        variaveis_registro['t2hiv_pep'] += registro.t2hiv_pep
        variaveis_registro['t2hiv_laboratorio'] += registro.t2hiv_laboratorio
        variaveis_registro['t2hiv_total_realizado'] += registro.t2hiv_total_realizado
        variaveis_registro['t2hiv_invalido'] += registro.t2hiv_invalido
        variaveis_registro['t2hiv_perdido'] += registro.t2hiv_perdido
        variaveis_registro['t2hiv_total_reagentes'] += registro.t2hiv_total_reagentes
        variaveis_registro['t2hiv_testes_estoque'] += registro.t2hiv_testes_estoque
        variaveis_registro['t2hiv_caixas_solicitadas'] += registro.t2hiv_caixas_solicitadas

        variaveis_registro['sifilis_cegonha'] += registro.sifilis_cegonha
        variaveis_registro['sifilis_rotina'] += registro.sifilis_rotina
        variaveis_registro['sifilis_mobilizacao'] += registro.sifilis_mobilizacao
        variaveis_registro['sifilis_upa'] += registro.sifilis_upa
        variaveis_registro['sifilis_pep'] += registro.sifilis_pep
        variaveis_registro['sifilis_laboratorio'] += registro.sifilis_laboratorio
        variaveis_registro['sifilis_total_realizado'] += registro.sifilis_total_realizado
        variaveis_registro['sifilis_invalido'] += registro.sifilis_invalido
        variaveis_registro['sifilis_perdido'] += registro.sifilis_perdido
        variaveis_registro['sifilis_total_reagentes'] += registro.sifilis_total_reagentes
        variaveis_registro['sifilis_testes_estoque'] += registro.sifilis_testes_estoque
        variaveis_registro['sifilis_caixas_solicitadas'] += registro.sifilis_caixas_solicitadas

        variaveis_registro['hepatiteb_cegonha'] += registro.hepatiteb_cegonha
        variaveis_registro['hepatiteb_rotina'] += registro.hepatiteb_rotina
        variaveis_registro['hepatiteb_mobilizacao'] += registro.hepatiteb_mobilizacao
        variaveis_registro['hepatiteb_upa'] += registro.hepatiteb_upa
        variaveis_registro['hepatiteb_pep'] += registro.hepatiteb_pep
        variaveis_registro['hepatiteb_laboratorio'] += registro.hepatiteb_laboratorio
        variaveis_registro['hepatiteb_total_realizado'] += registro.hepatiteb_total_realizado
        variaveis_registro['hepatiteb_invalido'] += registro.hepatiteb_invalido
        variaveis_registro['hepatiteb_perdido'] += registro.hepatiteb_perdido
        variaveis_registro['hepatiteb_total_reagentes'] += registro.hepatiteb_total_reagentes
        variaveis_registro['hepatiteb_testes_estoque'] += registro.hepatiteb_testes_estoque
        variaveis_registro['hepatiteb_caixas_solicitadas'] += registro.hepatiteb_caixas_solicitadas

        variaveis_registro['hepatitec_cegonha'] += registro.hepatitec_cegonha
        variaveis_registro['hepatitec_rotina'] += registro.hepatitec_rotina
        variaveis_registro['hepatitec_mobilizacao'] += registro.hepatitec_mobilizacao
        variaveis_registro['hepatitec_upa'] += registro.hepatitec_upa
        variaveis_registro['hepatitec_pep'] += registro.hepatitec_pep
        variaveis_registro['hepatitec_laboratorio'] += registro.hepatitec_laboratorio
        variaveis_registro['hepatitec_total_realizado'] += registro.hepatitec_total_realizado
        variaveis_registro['hepatitec_invalido'] += registro.hepatitec_invalido
        variaveis_registro['hepatitec_perdido'] += registro.hepatitec_perdido
        variaveis_registro['hepatitec_total_reagentes'] += registro.hepatitec_total_reagentes
        variaveis_registro['hepatitec_testes_estoque'] += registro.hepatitec_testes_estoque
        variaveis_registro['hepatitec_caixas_solicitadas'] += registro.hepatitec_caixas_solicitadas

        variaveis_registro['auto_teste_hiv'] += registro.auto_teste_hiv
        variaveis_registro['auto_teste_hiv_estoque'] += registro.auto_teste_hiv_estoque
        variaveis_registro['auto_teste_hiv_solicitadas'] += registro.auto_teste_hiv_solicitadas
    todas_unidades = Unidade.objects.all()
    for unidade in todas_unidades:
        if unidade.apelido not in unidades:
            n_preenchidas.append(unidade.apelido)
    context = {
        'form': variaveis_registro,
        'ano': ano,
        'mes': mes,
        'unidades': todas_unidades,
        'n_preenchidas': n_preenchidas,
    }
    return render(request, 'controle/ver_controle.html', context)


@login_required
def controle_search(request):
    mes = request.GET.get('mes')
    ano = request.GET.get('ano')
    unidade = request.GET.get('unidade')
    page = request.GET.get('page', 1)
    registros = ControleTeste.objects.all().order_by(Cast('mes', IntegerField()), 'unidade')
    if mes and not mes == 'todos':
        registros = registros.filter(mes=mes)
    if ano and not ano == 'todos':
        registros = registros.filter(ano=ano)
    if unidade:
        registros = registros.filter(unidade__apelido__icontains=unidade)

    paginator = Paginator(registros, 10)
    page_range = paginator.get_elided_page_range(number=page)
    try:
        registros = paginator.page(page)
    except PageNotAnInteger:
        registros = paginator.page(1)
    except EmptyPage:
        registros = paginator.page(paginator.num_pages)
    context = {
        'controles': registros,
        'page_range': page_range,
    }
    request.session['mes'] = mes
    request.session['ano'] = ano
    request.session['unidade'] = unidade
    return render(request, 'controle/partials/controle_tabela.html', context)


@login_required
def controle_export(request):
    mes = request.GET.get('mes')
    ano = request.GET.get('ano')
    registros = ControleTeste.objects.order_by(Cast('mes', IntegerField()), 'ano').values('ano', 'mes').distinct()
    if mes and not mes == 'todos':
        registros = registros.filter(mes=mes)
    if ano and not ano == 'todos':
        registros = registros.filter(ano=ano)
    page = request.GET.get('page', 1)
    paginator = Paginator(registros, 10)
    page_range = paginator.get_elided_page_range(number=page)
    try:
        registros = paginator.page(page)
    except PageNotAnInteger:
        registros = paginator.page(1)
    except EmptyPage:
        registros = paginator.page(paginator.num_pages)
    context = {
        'controles': registros,
        'page_range': page_range,
        'escolhas_meses': MES_CHOICES,
    }

    request.session['mes'] = mes
    request.session['ano'] = ano
    return render(request, 'controle/partials/controle_export.html', context)
