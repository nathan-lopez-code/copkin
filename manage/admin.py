from django.contrib import admin
from .models import Categorie, Article, Promotion, MesInformation

from django import forms


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        exclude = [
            "date_creation", "genre"
        ]
        widgets = {

            "nom": forms.TextInput(attrs={'class': 'form-control round-found'}),
            "description": forms.Textarea(attrs={'class': 'form-control round-found'}),

        }


class ArticleAdmin(admin.ModelAdmin):
    form = ArticleForm
    list_per_page = 15

    fieldsets = (
        (None, {
            'fields': ('nom', 'prix', 'description')
        }),
        ("image relative a l'article",
         {
             'fields': ('image1', 'image2', 'image3')
         }),
        (None, {
            'fields': ('categorie',)
        })
    )

    # list_filter = ("categorie", 'date_creation')
    search_fields = ['nom']
    list_display = ('nom', 'prix', 'date_creation')


class CategorieAdmin(admin.ModelAdmin):
    view_on_site = False
    list_display = ('nom', 'produit')

    @admin.display(description="nombre produit")
    def produit(self, categorie):
        return f"{len(categorie.article_set.all())} Articles"


class MesInformationAdmin(admin.ModelAdmin):
    view_on_site = False

    list_display = ('numero_whatsapp', 'autre_numero', 'adresse', 'email')
    list_display_links = None


class PromotionAdmin(admin.ModelAdmin):
    view_on_site = False

    list_display = ('nom', 'produit', 'active', )


admin.site.register(Categorie, CategorieAdmin)
admin.site.register(Promotion, PromotionAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(MesInformation, MesInformationAdmin)
