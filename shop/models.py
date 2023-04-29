from django.db import models
from manage.models import Article


class CardModel(models.Model):
    date = models.DateField(auto_now=True)
    message = models.TextField(max_length=500000,)