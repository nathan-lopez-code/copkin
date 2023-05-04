from django.urls import path
from .views import home_api, list_article, list_categorie, list_promotion, article_categorie, mes_informatiion

app_name = "api"


urlpatterns = [
    path('', home_api, name="home_api"),
    path('list/article', list_article, name="list_article"),
    path('list/categorie', list_categorie, name="list_categorie"),
    path('list/promotion', list_promotion, name="list_promotion"),
    path('mesinfo', mes_informatiion, name="mes_informations"),
    path('list/categorie/<int:id_categorie>/article', article_categorie, name="article_categorie"),
]
