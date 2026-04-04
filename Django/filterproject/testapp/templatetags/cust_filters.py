from django import template
from django.core.checks import register
register =template.Library()

def first_five_upper(value):
    result=value[:5].upper()
    return result
def first_n_upper(value,n):
    result=value[:n].upper()
    return result
register.filter("fnu",first_n_upper)
register.filter("ffu",first_five_upper)