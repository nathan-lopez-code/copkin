from django.urls import path
from .views import home, contact, detail, shopping, search, sell, card, cardBuy


app_name = 'shop_app'

urlpatterns = [
    path('', home, name='home_shop'),
    path('contact', contact, name='contact_shop'),
    path('produits', shopping, name='shopping_shop'),
    path('produits/detail?<int:pk>', detail, name='detail_shop'),
    path('produits/search?', search, name='search'),
    path('vendre', sell, name="sell_shop"),
    path('panier', card, name="card_shop"),
    path('sellPanier', cardBuy, name="cardbuy_shop"),
]
