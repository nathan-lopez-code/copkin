import json
from django.http.response import JsonResponse

from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from .forms import SearchFrom
from manage.models import Categorie, Article, Promotion, MesInformation
from django.core.paginator import Paginator


def price(query, strr):
    a = int(strr.split('-', 2)[1])
    b = int(strr.split('-', 2)[2])
    list_query = []
    for article in query:
        if a < article.prix < b:
            list_query.append(article)

    return list_query


def home(request):
    categories = Categorie.objects.all()
    recent = list(Article.objects.all())

    promotion = Promotion.objects.filter(active=True)[:2]
    info = MesInformation.objects.get(pk=1)
    context = {'categories': categories, 'recent': recent, 'active_id': recent[0].id,
               'promotions': promotion, 'recent4': Article.objects.all()[:4], 'form': SearchFrom,
               'mail': info.email,
               'numero': info.numero_whatsapp,
               "autre_numero": info.autre_numero,
               'adresse': info.adresse,
               }

    return render(request, 'shop/home.html', context)


def contact(request):
    """pqge de contact """

    info = MesInformation.objects.get(pk=1)
    context = {
        'form': SearchFrom,
        'mail': info.email,
        'numero': info.numero_whatsapp,
        "autre_numero": info.autre_numero,
        'adresse': info.adresse,
        'categories': Categorie.objects.all()
    }
    return render(request, 'shop/contact.html', context)


def shopping(request):
    categories = Categorie.objects.all()
    articles = Article.objects.all()
    paginator = Paginator(articles, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    query = []
    info = MesInformation.objects.get(pk=1)

    if not request.GET.get('categorie-all'):
        for categorie in categories:
            if request.GET.get(f"categorie-{categorie.id}"):
                listeEvaleur = list(categorie.article_set.all())
                query.extend(listeEvaleur)

        articles = query

    if not request.GET.get('price-all'):

        query = []

        if request.GET.get('price-0-50'):
            query.extend(price(articles, 'price-0-50'))

        if request.GET.get('pprice-50-100'):
            query.extend(price(articles, 'price-50-100'))

        if request.GET.get('price-100-300'):
            query.extend(price(articles, 'price-100-300'))

        if request.GET.get('price-300-700'):
            query.extend(price(articles, 'price-300-700'))

        if request.GET.get('price-700-inf'):
            query.extend(price(articles, 'price-700-99999999999'))

    if query:
        paginator = Paginator(query, 4)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

    return render(request, 'shop/shop.html', {
        'categories': categories, 'promotions': Promotion.objects.filter(active=True),
        'articles': articles,
        'page_obj': page_obj,
        'form': SearchFrom,
        'mail': info.email,
        'numero': info.numero_whatsapp,
        "autre_numero": info.autre_numero,
        'adresse': info.adresse,
    })


def detail(request, pk):

    info = MesInformation.objects.get(pk=1)

    try:
        article = Article.objects.get(id=pk)
        simulaire = article.categorie.article_set.exclude(nom=article.nom)[:5]
        promo = False
        ppromo = 0

        try:
            p = Promotion.objects.get(produit__id=article.id)
            if p.active:
                ppromo = p.pourcent
                promo = True
        except Exception as e:
            pass

        return render(request, 'shop/article.html', {
            'article': article, 'simulaire': simulaire,
            'articles': Article.objects.all()[:5],
            'promotions': Promotion.objects.all()[:2],
            'form': SearchFrom,
            'promoactive': promo,
            'ppromo': ppromo,
            'categories': Categorie.objects.all(),
            'mail': info.email,
            'numero': info.numero_whatsapp,
            "autre_numero": info.autre_numero,
            'adresse': info.adresse,


        })

    except Exception as e:
        return HttpResponse(f"Erreur 404 : {e}")


def search(request):

    nom = request.GET['nom']
    info = MesInformation.objects.get(pk=1)
    try:
        articles = Article.objects.filter(nom__contains=nom) or Article.objects.filter(categorie__nom__contains=nom)
    except Exception as e:
        articles = None
    paginator = Paginator(articles, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'key': nom, 'page_obj': page_obj, 'categories': Categorie.objects.all(), 'form': SearchFrom,
               'mail': info.email,
               'numero': info.numero_whatsapp,
               "autre_numero": info.autre_numero,
               'adresse': info.adresse,
               }

    return render(request, 'shop/search.html', context)


def sell(request):

    search = SearchFrom()

    info = MesInformation.objects.get(pk=1)
    context = {
        'form': search,
        'mail': info.email,
        'numero': info.numero_whatsapp,
        "autre_numero": info.autre_numero,
        'adresse': info.adresse,
        'categories': Categorie.objects.all(),
    }
    return render(request, 'shop/sell.html', context)


def card(request):
    search = SearchFrom()

    info = MesInformation.objects.get(pk=1)

    context = {
        'form': search,
        'mail': info.email,
        'numero': info.numero_whatsapp,
        "autre_numero": info.autre_numero,
        'adresse': info.adresse,
        'categories': Categorie.objects.all(),
    }

    return render(request, "shop/card.html", context)


def cardBuy(request):



#     from PIL import Image
#
#     imagePlage = Image.open("plage.jpg")
#     imageChat = Image.open("chat.jpg")
#
#     imagePlage = imagePlage.convert("RGBA")
#     imageChat = imageChat.convert("RGBA")
#
#     imagePlage.alpha_composite(imageChat, dest=(0, 0))
#
#     imagePlage.save("result.png")
#     imagePlage.show()
#     return render(request, "shop/confirm_commade.html", None)

    #return redirect("https://google.com")

    data = "no data"

    if request.POST:
        jsonData = json.loads(request.body)

        cardITem = jsonData.get("cardItem")
        data = cardITem
        return JsonResponse({"data": data})

    return HttpResponse(data)
