from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from .models import Log

ACOES = [
    'login-failed',
    'login',
    'update',
    'password-reset',
    'create',
    'delete',
    'logout',
]

@login_required
@user_passes_test(lambda u: u.is_superuser, login_url='home')
def view_logs(request):
    logs = Log.objects.all().order_by('-data_hora')
    usuarios = []
    users = Log.objects.all().values('usuario').distinct()
    for user in users:
        if user['usuario'] not in usuarios:
            usuarios.append(user['usuario'])
    page = request.GET.get('page', 1)
    paginator = Paginator(logs, 10)
    page_range = paginator.get_elided_page_range(number=page)
    try:
        logs = paginator.page(page)
    except PageNotAnInteger:
        logs = paginator.page(1)
    except EmptyPage:
        logs = paginator.page(paginator.num_pages)
    context = {
        'logs': logs,
        'page_range': page_range,
        'usuarios': usuarios,
        'acoes': ACOES,
    }
    return render(request, 'log/view_logs.html', context)


@login_required
@user_passes_test(lambda u: u.is_superuser, login_url='home')
def view_log(request, pk):
    log = Log.objects.get(pk=pk)
    context = {
        'log': log,
    }
    return render(request, 'log/log.html', context)


@login_required
@user_passes_test(lambda u: u.is_superuser, login_url='home')
def log_search(request):
    acao = request.GET.get('acao')
    usuario = request.GET.get('usuario')
    usuarios = []
    users = Log.objects.all().values('usuario').distinct()
    for user in users:
        if user['usuario'] not in usuarios:
            usuarios.append(user['usuario'])
    logs = Log.objects.all().order_by('-data_hora')
    if acao and not acao == 'todas':
        logs = logs.filter(acao=acao)
    if usuario and not usuario == 'todos' and usuario != 'None':
        logs = logs.filter(usuario=usuario)
    elif usuario == 'None':
        logs = logs.filter(usuario__isnull=True)
    page = request.GET.get('page', 1)
    paginator = Paginator(logs, 10)
    page_range = paginator.get_elided_page_range(number=page)
    try:
        logs = paginator.page(page)
    except PageNotAnInteger:
        logs = paginator.page(1)
    except EmptyPage:
        logs = paginator.page(paginator.num_pages)
    request.session['acao'] = acao
    request.session['usuario'] = usuario
    context = {
        'logs': logs,
        'page_range': page_range,
        'usuarios': usuarios,
        'acoes': ACOES,
    }
    return render(request, 'log/partials/log_table.html', context)
