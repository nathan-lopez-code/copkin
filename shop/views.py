from django.shortcuts import render
from django.http.response import HttpResponse
from .forms import SearchFrom
from manage.models import Categorie, Article, Promotion
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

    context = {'categories': categories, 'recent': recent, 'active_id': recent[0].id,
               'promotions': promotion, 'recent4': Article.objects.all()[:4], 'form': SearchFrom}

    return render(request, 'shop/home.html', context)


def contact(request):
    """pqge de contact """

    context = {
        'form': SearchFrom,
        'mail': "copkin21@gmail.com",
        'numero': "+243 850411990",
        'adresse': "ville de kinsasha",
        'categories': Categorie.objects.all()
    }
    return render(request, 'shop/contact.html', context)


def shopping(request):
    categories = Categorie.objects.all()
    articles = Article.objects.all()
    paginator = Paginator(articles, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    query = []

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
    })



def detail(request, pk):

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
            'categories': Categorie.objects.all()
        })

    except Exception as e:
        return HttpResponse(f"Erreur 404 : {e}")


def search(request):

    nom = request.GET['nom']
    try:
        articles = Article.objects.filter(nom__contains=nom) or Article.objects.filter(categorie__nom__contains=nom)
    except Exception as e:
        articles = None
    paginator = Paginator(articles, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'key': nom, 'page_obj': page_obj, 'categories': Categorie.objects.all(), 'form': SearchFrom}

    return render(request, 'shop/search.html', context)
