from django.shortcuts import render
from django.http.response import HttpResponse
from manage.models import Categorie


def home(request):

    categories = Categorie.objects.all()

    context = {'categories': categories}

    return render(request, 'shop/home.html', context)


def contact(request):
    """pqge de contact """
    return HttpResponse("site en cours de developpement, page de contact ici")


def shopping(request):
    return HttpResponse("site en cours de developpement, page de tout nos article")


def categorie(request, categorie):

    return HttpResponse('cool')


def detail(request, pk):
    return HttpResponse(f"site en cours de developpement, ici detail article nom ; {pk}")
