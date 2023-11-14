from django.db.models.signals import post_save, pre_save, pre_delete
from django.contrib.auth.models import User
from log.models import Log
from django.dispatch import receiver
from .models import ControleTeste


# Verificar o post_save e Pre_Save
@receiver(pre_save, sender=ControleTeste)
def controle_teste_pre_save(sender, instance, **kwargs):
    if instance.pk:
        # Obtém os dados antes da atualização
        # Início 'Gambiarra'
        import inspect
        request = None
        for fr in inspect.stack():
            if fr[3] == 'get_response':
                request = fr[0].f_locals['request']
                break
        usuario = User.objects.get(pk=request.user.pk)
        # Fim 'Gambiarra'
        original_instance = sender.objects.get(pk=instance.pk)
        dados_antes = {field.name: getattr(original_instance, field.name) for field in instance._meta.fields}
    else:
        # Caso seja uma criação, não há dados antes
        # Início 'Gambiarra'
        import inspect
        request = None
        for fr in inspect.stack():
            if fr[3] == 'get_response':
                request = fr[0].f_locals['request']
                break
        usuario = User.objects.get(pk=request.user.pk)
        # Fim 'Gambiarra'
        dados_antes = None
    dados_depois = {field.name: getattr(instance, field.name) for field in instance._meta.fields}

    Log.objects.create(
        usuario=usuario,
        acao='create' if not instance.pk else 'update',
        objeto_afetado=f'{sender.__name__} "{instance.unidade.apelido}" {instance.ano} / {instance.mes}',
        mensagem=f'Controle {instance.pk} foi criada' if not instance.pk else f'Controle "{instance.unidade.apelido}" {instance.ano} / {instance.mes} foi atualizada',
        dados_antes=dados_antes,
        dados_depois=dados_depois,
    )


@receiver(pre_delete, sender=ControleTeste)
def pre_delete_seu_modelo(sender, instance, **kwargs):
    # Crie um registro de log antes de excluir o objeto
    # Início 'Gambiarra'
    import inspect
    request = None
    for fr in inspect.stack():
        if fr[3] == 'get_response':
            request = fr[0].f_locals['request']
            break
    usuario = User.objects.get(pk=request.user.pk)
    # Fim 'Gambiarra'
    log = Log(
        usuario=usuario,
        acao='delete',
        objeto_afetado=f'{sender.__name__} "{instance.unidade.apelido}" {instance.ano} / {instance.mes}',
        mensagem=f'{sender.__name__} "{instance.unidade.apelido}" {instance.ano} / {instance.mes} foi excluído',
        dados_antes={field.name: getattr(instance, field.name) for field in instance._meta.fields},
    )
    log.save()
