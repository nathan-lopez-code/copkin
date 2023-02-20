from django import template

register = template.Library()


@register.filter
def four(query):
    return query[:4]


@register.filter
def reduction(prix):
    return round(prix * 1.7, 2)


@register.filter
def mini(text, value):
    return f"{text[:value]}..."


@register.filter
def number(query, number):
    return query[-number:]


@register.filter
def spromo(value, reduct):
    return int((value * reduct) / 100)


@register.filter
def price(query, strr):
    a = int(strr.split('-', 2)[0])
    b = int(strr.split('-', 2)[1])
    list_query = []
    for article in query:
        if a < article.prix < b:
            list_query.append(article)

    return len(list_query)