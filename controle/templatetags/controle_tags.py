from django import template
from controle.models import MES_CHOICES

register = template.Library()


@register.filter
def month_string(value):
    return MES_CHOICES[int(value) - 1][1]

