from django.urls import path
from .views import home, categorie, contact, detail, shopping


app_name = 'shop_app'

urlpatterns = [
    path('', home, name='home_shop'),
    path('contact', contact, name='contact_shop'),
    path('produits', shopping, name='shopping_shop'),
    path('produits/categorie?<str:categorie>', categorie, name='categorie_shop'),
    path('produits/detail?<int:pk>', detail, name='detail_shop'),
]