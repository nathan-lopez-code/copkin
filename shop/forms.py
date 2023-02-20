from django import forms


class SearchFrom(forms.Form):
    nom = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "ex : Iphone 13"}))
