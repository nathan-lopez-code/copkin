# Generated by Django 4.1.6 on 2023-02-19 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage', '0003_article_date_creation_promotion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promotion',
            name='pourcent',
            field=models.IntegerField(blank=True, null=True, verbose_name='pourcentage de reduction'),
        ),
    ]
