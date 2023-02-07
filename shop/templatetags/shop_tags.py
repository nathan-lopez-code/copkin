from django import template

register = template.Library()


@register.filter
def four(query):
    return query[:4]


@register.filter
def reduction(prix):
    return round(prix * 2.4, 2)