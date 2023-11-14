from datetime import datetime
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.hashers import make_password
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from accounts.forms import UserForm
from accounts.models import UserProfile
from unidades.models import Unidade
from django.utils.safestring import mark_safe


@login_required
@staff_member_required(login_url='users')
def users(request):
    users_list = User.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(users_list, 10)
    page_range = paginator.get_elided_page_range(number=page)
    try:
        users_list = paginator.page(page)
    except PageNotAnInteger:
        users_list = paginator.page(1)
    except EmptyPage:
        users_list = paginator.page(paginator.num_pages)
    context = {
        'users': users_list,
        'page_range': page_range,
    }
    return render(request, 'accounts/user_list.html', context)


@login_required
@staff_member_required(login_url='users')
def user_create(request):
    unidades = Unidade.objects.all()
    if request.method == "POST":
        formulario = UserForm(request.POST)
        try:
            unidade = Unidade.objects.get(cnes=request.POST.get('unidade'))
            if formulario.is_valid():
                formulario = User.objects.create_user(
                    username=formulario.cleaned_data['username'],
                    first_name=formulario.cleaned_data['first_name'],
                    email=formulario.cleaned_data['email'],
                    is_staff=formulario.cleaned_data['is_staff'],
                    is_superuser=formulario.cleaned_data['is_superuser'],
                    password='1234'
                )
                perfil = UserProfile(user=formulario, created_by=request.user, updated_by=request.user, unidade=unidade)
                perfil.save()

                messages.add_message(request=request, message='Usuário cadastrado com sucesso!',
                                     level=messages.SUCCESS)
                return redirect('users')
            else:
                messages.add_message(request=request, message='Ocorreu um erro ao cadastrar o usuário!',
                                     level=messages.ERROR)
                return render(request, 'accounts/user_create.html', {'form': formulario, 'unidades': unidades})
        except Exception as ex:
            messages.add_message(request=request, message=mark_safe(f'Ocorreu um erro não especificado ao cadastrar o usuário! Entre em contato e informe a mensagem: <br/> {ex}'),
                                 level=messages.ERROR)
            context = {
                'form': formulario,
                'unidades': unidades,
            }
            return render(request, 'accounts/user_create.html', context)
    else:
        context = {
            'form': UserForm(),
            'unidades': unidades,
        }
        return render(request, 'accounts/user_create.html', context)


@login_required
@staff_member_required(login_url='users')
def user_edit(request, pk):
    unidades = Unidade.objects.all()
    if request.method == "POST":
        try:
            user = User.objects.get(pk=pk)
            form = UserForm(request.POST, instance=user)
            unidade = Unidade.objects.get(cnes=request.POST.get('unidade'))

            if form.is_valid():
                data = {
                    'unidade': unidade,
                    'updated_by': request.user,
                    'updated_at': datetime.now(),
                }
                form.save()
                user_profile = UserProfile.objects.get(user_id=pk)

                if user_profile:
                    for key, value in data.items():
                        setattr(user_profile, key, value)
                    user_profile.save()

                messages.add_message(request=request, message='Usuário atualizado com sucesso!',
                                     level=messages.SUCCESS)
                return redirect('users')
            else:
                messages.add_message(request=request, message=f'Ocorreu um erro. Verifique os campos preenchidos.',
                                     level=messages.ERROR)
                user = User.objects.get(pk=pk)
                profile = UserProfile.objects.get(user_id=pk)
                context = {
                    'user': user,
                    'form': form,
                    'profile': profile,
                    'unidades': unidades,
                }
                return render(request, 'accounts/user_edit.html', context)
        except Exception as ex:
            messages.add_message(request=request, message=mark_safe(f'Ocorreu um erro não especificado ao cadastrar o usuário! Entre em contato e informe a mensagem: <br/> {ex}'),
                                 level=messages.ERROR)
            user = User.objects.get(pk=pk)
            form = UserForm(request.POST, instance=user)
            profile = UserProfile.objects.get(user_id=pk)
            context = {
                'user': user,
                'form': form,
                'profile': profile,
                'unidades': unidades,
            }
            return render(request, 'accounts/user_edit.html', context)
    else:
        unidades = Unidade.objects.all()
        user = User.objects.get(pk=pk)
        form = UserForm(instance=user)
        profile = UserProfile.objects.get(user_id=pk)
        context = {
            'user': user,
            'form': form,
            'profile': profile,
            'unidades': unidades,
        }
        return render(request, 'accounts/user_edit.html', context)


@login_required
@staff_member_required(login_url='users')
def users_search(request):
    nome = request.GET.get('nome')
    email = request.GET.get('email')
    page = request.GET.get('page', 1)
    users = User.objects.all()
    if nome:
        users = users.filter(first_name__icontains=nome)
    if email:
        users = users.filter(email__icontains=email)

    paginator = Paginator(users, 10)
    page_range = paginator.get_elided_page_range(number=page)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    context = {
        'users': users,
        'page_range': page_range,
    }
    request.session['nome'] = nome
    request.session['email'] = email
    return render(request, 'accounts/partials/users_table.html', context)
