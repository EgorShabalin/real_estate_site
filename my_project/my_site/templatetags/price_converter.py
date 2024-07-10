from django import template
from ..utils import get_usd, get_eur, get_rub

register = template.Library()


@register.filter
def usd(value):
    return get_usd(value)


@register.filter
def eur(value):
    return get_eur(value)


@register.filter
def rub(value):
    return get_rub(value)
