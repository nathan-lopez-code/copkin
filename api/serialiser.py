from rest_framework import serializers as s



class ArticleSerialiser(s.Serializer):
    id = s.IntegerField(read_only=True)
    nom = s.CharField(max_length=100)
    prix = s.IntegerField()
    description = s.CharField(max_length=3000)

    image1 = s.ImageField()
    image2 = s.ImageField()
    image3 = s.ImageField()

    categorie = s.CharField(max_length=20)

    genre = s.CharField(max_length=100)

    date_creation = s.DateField()


class CategorieSerialiser(s.Serializer):
    id = s.IntegerField(read_only=True)
    nom = s.CharField(max_length=100)
    images = s.ImageField()


class PromotionSerialiser(s.Serializer):
    id = s.IntegerField(read_only=True)
    nom = s.CharField(max_length=200)
    description = s.CharField(max_length=500)
    produit = s.CharField(max_length=20)
    pourcent = s.IntegerField()
    date_de_creation = s.DateTimeField()

