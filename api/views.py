from django.http.response import JsonResponse
from manage.models import Promotion, Article, Categorie
from .serialiser import PromotionSerialiser, ArticleSerialiser, CategorieSerialiser


def list_article(request):

    reponse = {
        'articles': ArticleSerialiser(Article.objects.all(), many=True).data,
    }
    return JsonResponse(reponse)


def list_categorie(request):

    return JsonResponse(
        {'categories': CategorieSerialiser(Categorie.objects.all(), many=True).data}
    )


def list_promotion(request):

    return JsonResponse(
        {'promotions': PromotionSerialiser(Promotion.objects.filter(active=True), many=True).data}
    )


def article_categorie(request, id_categorie):
    try:
        query = Categorie.objects.get(pk=id_categorie).article_set
    except Exception as e:
        return JsonResponse({'error': 404},safe=True)

    response = {'articles': ArticleSerialiser(query, many=True).data}

    return JsonResponse(
        response
    )


def home_api(request):

    response = {
        'promotions': PromotionSerialiser(Promotion.objects.filter(active=True), many=True).data,
        'categories': CategorieSerialiser(Categorie.objects.all(), many=True).data,
        'Articles': ArticleSerialiser(Article.objects.all(), many=True).data,
    }

    return JsonResponse(response)
