from django.db import models
from django.urls import reverse
import os


def delete_util(image):
    try:
        os.remove(image.path)
    except Exception as e:
        pass


class Categorie(models.Model):
    nom = models.CharField(max_length=100)
    images = models.ImageField(
        upload_to='categorie/', blank=True, null=True, verbose_name="image representative d'une categorie"
    )

    def __str__(self):
        return f"{self.nom}"

    def get_absolute_url(self):
        return reverse('shop_app:categorie_shop', kwargs={'categorie' : self.nom})

    def delete(self, *args, **kwargs):
        try:
            os.remove(self.images.path)
        except Exception as e:
            print(e)
        super().delete(*args, **kwargs)


class Article(models.Model):
    nom = models.CharField(max_length=100)
    prix = models.IntegerField()
    description = models.TextField(max_length=3000, null=True, blank=True)

    # images
    image1 = models.ImageField(upload_to='articles/')
    image2 = models.ImageField(upload_to='articles/', null=True, blank=True)
    image3 = models.ImageField(upload_to='articles/', null=True, blank=True)

    # categorie
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)

    # genre
    genre = models.CharField(max_length=100, null=True, blank=True)

    # type a la mode

    date_creation = models.DateField(null=True, blank=True, auto_now=True)

    def __str__(self):
        return f'{self.nom}'

    def get_absolute_url(self):
        return reverse('shop_app:detail_shop', kwargs={'pk': self.id})

    def delete(self, *args, **kwargs):
        delete_util(self.image1)
        delete_util(self.image2)
        delete_util(self.image3)
        super().delete(*args, **kwargs)

    class Meta:
        ordering = ['-date_creation']


class Promotion(models.Model):
    nom = models.CharField(max_length=200, default="mega promotiom et solde")
    description = models.CharField(verbose_name='description de la promotion', max_length=500, blank=True, null=True)
    produit = models.ForeignKey(Article, verbose_name='produit associer', on_delete=models.CASCADE)
    pourcent = models.IntegerField(verbose_name='pourcentage de reduction', null=True, blank=True)

    active = models.BooleanField(verbose_name="etat d'activation de la promotion", default=False)

    date_de_creation = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return f"promotion de {self.pourcent}% sur {self.produit.nom}"

    class Meta:
        ordering = ['-date_de_creation']


class MesInformation(models.Model):

    nom_du_site = models.CharField(default="copkin", max_length=30, editable=False)
    numero_whatsapp = models.CharField(
        default="243850411990", help_text=" ex : 24398765795 (Sans espace ni +", max_length=16)
    autre_numero = models.CharField(
        default="243850411990", help_text=" ex : 24398765795 (Sans espace ni +", max_length=16)

    adresse = models.CharField(max_length=200, default="ville de kinshasa")
    email = models.EmailField()






