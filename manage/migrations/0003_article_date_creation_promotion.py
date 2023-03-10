# Generated by Django 4.1.6 on 2023-02-19 16:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manage', '0002_article'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='date_creation',
            field=models.DateField(auto_now=True, null=True),
        ),
        migrations.CreateModel(
            name='Promotion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(default='mega promotiom et solde', max_length=200)),
                ('pourcent', models.IntegerField(blank=True, null=True)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('produit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manage.article')),
            ],
        ),
    ]
