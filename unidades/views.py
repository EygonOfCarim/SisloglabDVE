from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db import IntegrityError
from django.db.models.functions import Cast
from django.shortcuts import render, redirect
from accounts.models import UserProfile
from django.db.models import IntegerField
from .models import Unidade
import requests
from requests import JSONDecodeError, ReadTimeout, ConnectTimeout
from datetime import datetime
from django.utils.safestring import mark_safe


UF = {
    'AC': 'Acre',
    'AL': 'Alagoas',
    'AP': 'Amapá',
    'AM': 'Amazonas',
    'BA': 'Bahia',
    'CE': 'Ceará',
    'DF': 'Distrito Federal',
    'ES': 'Espírito Santo',
    'GO': 'Goiás',
    'MA': 'Maranhão',
    'MT': 'Mato Grosso',
    'MS': 'Mato Grosso do Sul',
    'MG': 'Minas Gerais',
    'PA': 'Pará',
    'PB': 'Paraíba',
    'PR': 'Paraná',
    'PE': 'Pernambuco',
    'PI': 'Piauí',
    'RJ': 'Rio de Janeiro',
    'RN': 'Rio Grande do Norte',
    'RS': 'Rio Grande do Sul',
    'RO': 'Rondônia',
    'RR': 'Roraima',
    'SC': 'Santa Catarina',
    'SP': 'São Paulo',
    'SE': 'Sergipe',
    'TO': 'Tocantins'
}


@login_required
def unidades(request):
    lista_unidades = Unidade.objects.all().order_by(
            Cast('cnes', IntegerField()))
    page = request.GET.get('page', 1)
    paginator = Paginator(lista_unidades, 5)
    page_range = paginator.get_elided_page_range(number=page)
    try:
        t_unidades = paginator.page(page)
    except PageNotAnInteger:
        t_unidades = paginator.page(1)
    except EmptyPage:
        t_unidades = paginator.page(paginator.num_pages)
    context = {
        'unidades': t_unidades,
        'page_range': page_range,
    }
    return render(request, 'unidades/listar_unidades.html', context)


@login_required
@staff_member_required(login_url='unidades')
def buscar_unidade(request):
    if request.method == 'POST':
        if Unidade.objects.filter(cnes=request.POST.get('cnes')):
            messages.add_message(request=request, message='CNES já cadastrado anteriormente!',
                                 level=messages.ERROR)
            return render(request, 'unidades/buscar_unidade.html', {'cnes': request.POST.get('cnes')})
        try:
            uf = 'SP'
            municipio = "RIBEIRAO PRETO"
            url = f"https://apidadosabertos.saude.gov.br/cnes/estabelecimentos/{request.POST.get('cnes')}"
            response = requests.get(url, timeout=5)
            response_json = response.json()
            if response_json['codigo_uf'] == 35:
                uf = 'SP'
            if response_json['codigo_municipio'] == 354340:
                municipio = "RIBEIRAO PRETO"
            context = {
                'cnes': response_json['codigo_cnes'],
                'razao_social': response_json['nome_razao_social'],
                'nome_fantasia': response_json['nome_fantasia'],
                'cep': response_json['codigo_cep_estabelecimento'],
                'endereco': response_json['endereco_estabelecimento'],
                'numero': response_json['numero_estabelecimento'] if response_json['numero_estabelecimento'].isnumeric() else 0,
                'bairro': response_json['bairro_estabelecimento'],
                'telefone': response_json['numero_telefone_estabelecimento'] if response_json['numero_telefone_estabelecimento'][0] != '0' else response_json['numero_telefone_estabelecimento'].lstrip(response_json['numero_telefone_estabelecimento'][0]),
                'uf': uf,
                'municipio': municipio,
                'ufs': UF,
            }
            return render(request, 'unidades/criar_unidade.html', context)
        except (JSONDecodeError, KeyError):
            messages.add_message(request=request, message='A busca não retornou dados válidos. Verifique o número do CNES e tente novamente!',
                                 level=messages.ERROR)
            return render(request, 'unidades/buscar_unidade.html', {'cnes': request.POST.get('cnes')})
        except (ReadTimeout, ConnectTimeout) as ex:
            messages.add_message(request=request, message=mark_safe(f'A busca não retornou os dados dentro do tempo previsto. Entre com os dados manualmente ou tente novamente mais tarde!'),
                                 level=messages.ERROR)
            return redirect('criar_unidade')
        except Exception as ex:
            messages.add_message(request=request, message=mark_safe(f'Ocorreu um erro não especificado! Entre em contato e informe a mensagem: {ex}'),
                                 level=messages.ERROR)
            return render(request, 'unidades/buscar_unidade.html', {'cnes': request.POST.get('cnes')})
    else:
        context = {}
        return render(request, 'unidades/buscar_unidade.html', context)


@login_required
@staff_member_required(login_url='unidades')
def criar_unidade(request):
    if request.method == 'POST':
        try:
            Unidade.objects.create(
                cnes=request.POST.get('cnes'),
                razao_social=request.POST.get('razao_social'),
                apelido=request.POST.get('nome_fantasia'),
                cep=request.POST.get('cep'),
                endereco=request.POST.get('endereco'),
                numero=request.POST.get('numero'),
                bairro=request.POST.get('bairro'),
                uf=request.POST.get('uf'),
                municipio=request.POST.get('municipio'),
                telefone=request.POST.get('telefone'),
                created_by=request.user,
                updated_by=request.user,
            )
        except Exception as ex:
            messages.add_message(request=request, message=mark_safe(f'Ocorreu um erro não especificado ao cadastrar a unidade! Entre em contato e informe a mensagem: <br/> {ex}'),
                                 level=messages.ERROR)
            return render(request, 'unidades/buscar_unidade.html', {'cnes': request.POST.get('cnes')})
        messages.add_message(request=request, message='Unidade cadastrada com sucesso!',
                             level=messages.SUCCESS)
        return redirect('unidades')
    else:
        context = {}
        return render(request, 'unidades/buscar_unidade.html', context)


@login_required
@staff_member_required(login_url='unidades')
def editar_unidade(request, pk):
    unidade = Unidade.objects.get(pk=pk)
    usuario = UserProfile.objects.get(pk=request.user.id)
    if usuario.unidade == unidade or request.user.is_superuser:
        if request.method == "POST":
            data = {
                'cnes': request.POST.get('cnes'),
                'razao_social': request.POST.get('razao_social'),
                'apelido': request.POST.get('nome_fantasia'),
                'cep': request.POST.get('cep'),
                'endereco': request.POST.get('endereco'),
                'numero': request.POST.get('numero'),
                'bairro': request.POST.get('bairro'),
                'uf': request.POST.get('uf'),
                'municipio': request.POST.get('municipio'),
                'telefone': request.POST.get('telefone'),
                'updated_by': request.user,
                'updated_at': datetime.now(),
            }
            try:
                unidade_atualizada = Unidade.objects.get(pk=pk)
                if unidade_atualizada:
                    for key, value in data.items():
                        setattr(unidade_atualizada, key, value)
                    unidade_atualizada.save()
                messages.add_message(request=request, message='Unidade atualizada com sucesso!',
                                     level=messages.SUCCESS)
                return redirect('unidades')
            except Exception as ex:
                messages.add_message(request=request, message=mark_safe(f'Ocorreu um erro não especificado ao cadastrar a unidade! Entre em contato e informe a mensagem: <br/> {ex}'),
                                     level=messages.ERROR)
                return redirect('unidades')
        else:
            unidade = Unidade.objects.get(pk=pk)
            context = {
                'uf': UF,
                'unidade': unidade
            }
            return render(request, 'unidades/editar_unidade.html', context)
    else:
        return redirect('unidades')


@login_required
@staff_member_required(login_url='unidades')
def unidades_search(request):
    cnes = request.GET.get('cnes')
    apelido = request.GET.get('nome_fantasia')
    page = request.GET.get('page', 1)
    unidades = Unidade.objects.all().order_by(
            Cast('cnes', IntegerField()))
    if cnes:
        unidades = unidades.filter(cnes__icontains=cnes)
    if apelido:
        unidades = unidades.filter(apelido__icontains=apelido)

    paginator = Paginator(unidades, 5)
    page_range = paginator.get_elided_page_range(number=page)
    try:
        unidades = paginator.page(page)
    except PageNotAnInteger:
        unidades = paginator.page(1)
    except EmptyPage:
        unidades = paginator.page(paginator.num_pages)
    context = {
        'unidades': unidades,
        'page_range': page_range,
    }
    request.session['cnes'] = cnes
    request.session['apelido'] = apelido
    return render(request, 'unidades/partials/tabela_unidades.html', context)
