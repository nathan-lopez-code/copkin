from django.shortcuts import render
from django.http.response import HttpResponse
from .forms import SearchFrom
from manage.models import Categorie, Article, Promotion


def home(request):
    categories = Categorie.objects.all()
    recent = list(Article.objects.all())

    promotion = Promotion.objects.filter(active=True)[:2]

    context = {'categories': categories, 'recent': recent, 'active_id': recent[0].id,
               'promotions': promotion, 'recent4': Article.objects.all()[:4], 'form': SearchFrom}

    return render(request, 'shop/home.html', context)


def contact(request):
    """pqge de contact """
    return HttpResponse("site en cours de developpement, page de contact ici")


def shopping(request):

    return render(request, 'shop/shop.html', {'categories': Categorie.objects.all(), 'promotions': Promotion.objects.filter(active=True), 'articles': Article.objects.all()})

def categorie(request, categorie):

    return HttpResponse('cool')


def detail(request, pk):

    try:
        article = Article.objects.get(id=pk)
        simulaire = article.categorie.article_set.exclude(nom=article.nom)[:5]
        return render(request, 'shop/article.html', {
            'article': article, 'simulaire': simulaire
        })

    except Exception as e:
        return HttpResponse(f"Erreur 404 : {e}")


def search(request):
    try:
        nom = request.GET['nom']
        match = Article.objects.filter(nom__contains=nom) or Article.objects.filter(categorie__nom__contains=nom)
        return HttpResponse(match)

    except Exception as e:
        return HttpResponse("aucun resultat")