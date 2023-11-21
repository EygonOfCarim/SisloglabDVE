from django.contrib.auth.signals import user_login_failed, user_logged_in, user_logged_out
from django.db.models.signals import post_save, pre_delete, pre_save
from django.dispatch import receiver
from .models import Log
from unidades.models import Unidade
from django.contrib.auth.models import User
from accounts.models import UserProfile


@receiver(user_login_failed)
def log_login_failed(sender, credentials, request, **kwargs):
    username = credentials.get('username')
    password = credentials.get('password')

    Log.objects.create(
        usuario=None,
        acao='login-failed',
        objeto_afetado=f'Usuário utilizado: {username}',
        mensagem='Tentativa malsucedida de Login!',
        dados_antes={'username': username, 'password': password},
        dados_depois=None,
    )


@receiver(user_logged_in)
def log_login(sender, request, user, **kwargs):
    Log.objects.create(
        usuario=user,
        acao='login',
        objeto_afetado=user.username,
        mensagem='Efetuou login com sucesso!',
        dados_antes=None,
        dados_depois=None,
    )


@receiver(user_logged_out)
def log_logout(sender, request, user, **kwargs):
    Log.objects.create(
        usuario=user,
        acao='logout',
        objeto_afetado=user.username,
        mensagem='Efetuou logout com sucesso!',
        dados_antes=None,
        dados_depois=None,
    )


@receiver(pre_save, sender=Unidade)
def log_unidade_pre_save(sender, instance, **kwargs):
    if instance.pk:
        # Obtém os dados antes da atualização
        original_instance = sender.objects.get(pk=instance.pk)
        dados_antes = {field.name: getattr(original_instance, field.name) for field in instance._meta.fields}
    else:
        # Caso seja uma criação, não há dados antes
        dados_antes = None

    # Aqui você pode comparar os dados antes e depois se necessário
    dados_depois = {field.name: getattr(instance, field.name) for field in instance._meta.fields}

    Log.objects.create(
        usuario=instance.updated_by,  # Supondo que o campo seja updated_by
        acao='create' if not instance.pk else 'update',
        objeto_afetado=f'{sender.__name__} {instance.apelido}',
        mensagem=f'Unidade {instance.apelido} foi criada' if not instance.pk else f'Unidade {instance.apelido} foi atualizada',
        dados_antes=dados_antes,
        dados_depois=dados_depois,
    )


@receiver(pre_save, sender=UserProfile)
def user_profile_pre_save(sender, instance, **kwargs):
    if instance.pk:
        # Início 'Gambiarra'
        import inspect
        request = None
        for fr in inspect.stack():
            if fr[3] == 'get_response':
                request = fr[0].f_locals['request']
                break
        usuario = User.objects.get(pk=request.user.pk)
        # Fim 'Gambiarra'
        # Obtém os dados antes da atualização
        original_instance = sender.objects.get(pk=instance.pk)
        dados_antes = {field.name: getattr(original_instance, field.name) for field in instance._meta.fields}
    else:
        # Caso seja uma criação, não há dados antes
        dados_antes = None
        # Início 'Gambiarra'
        import inspect
        request = None
        for fr in inspect.stack():
            if fr[3] == 'get_response':
                request = fr[0].f_locals['request']
                break
        usuario = User.objects.get(pk=request.user.pk)
        # Fim 'Gambiarra'

    # Aqui você pode comparar os dados antes e depois se necessário
    dados_depois = {field.name: getattr(instance, field.name) for field in instance._meta.fields}

    Log.objects.create(
        usuario=usuario,  # Supondo que o campo seja updated_by
        acao='create' if not instance.pk else 'update',
        objeto_afetado=f'{sender.__name__} {instance.user.username}',
        mensagem=f'Usuário {instance.pk} foi criado' if not instance.pk else f'Usuário {instance.pk} foi atualizado',
        dados_antes=dados_antes,
        dados_depois=dados_depois,
    )
