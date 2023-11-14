from django import template
from django.contrib.auth.models import User
register = template.Library()


@register.filter
def user_name(value):
    try:
        user = User.objects.get(pk=value)
        return f'{user.username}'
    except:
        return 'Vazio'

