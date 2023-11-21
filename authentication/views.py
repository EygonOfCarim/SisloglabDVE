from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.views import PasswordResetView
from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from log.models import Log
from django.contrib.auth.views import PasswordResetView
from django.utils.translation import gettext as _
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator


def login_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        return render(request, 'authentication/login.html')


def login_process(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if not user.last_login:
                login(request, user)
                return redirect('first_access')
            else:
                if user.is_active:
                    login(request, user)
                    return redirect('home')
                else:
                    messages.add_message(request=request, message='Usuário não tem permissão de acesso!', level=messages.ERROR)
                    return render(request, 'authentication/login.html')
        else:
            context = {
                'username': username,
                'password': password
            }
            messages.add_message(request=request, message='Usuário ou senha incorretos!', level=messages.ERROR)
            return render(request, 'authentication/login.html', context)
    else:
        return render(request, 'authentication/login.html')


@login_required
def logout_process(request):
    logout(request)
    return redirect('home')


@login_required
def first_access(request):
    if request.method == 'POST':
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 == password2:
            password = make_password(password1)
            user = request.user
            try:
                validate_password(password1, user=user)
                user.set_password(password1)
                user.save()
                messages.add_message(request=request, message='Senha alterada com sucesso!', level=messages.SUCCESS)
                return redirect('home')
            except ValidationError as validate:
                messages.add_message(request=request, message=validate, level=messages.ERROR)
                return render(request, 'authentication/first_access.html')
        else:
            messages.add_message(request=request, message='Senhas não são iguais!', level=messages.ERROR)
            return render(request, 'authentication/first_access.html')
    else:
        return render(request, 'authentication/first_access.html')


class CustomPasswordResetView(PasswordResetView):
    def form_valid(self, form):
        email = form.cleaned_data['email']

        Log.objects.create(
            usuario=None,
            acao='password-reset',
            objeto_afetado=None,
            mensagem=f'Solicitação de reset de senha pelo e-mail: {email}',
            dados_antes=None,
            dados_depois=None,
        )

        return super().form_valid(form)
