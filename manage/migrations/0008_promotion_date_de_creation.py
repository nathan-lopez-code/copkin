# Generated by Django 4.1.6 on 2023-02-19 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage', '0007_alter_promotion_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='promotion',
            name='date_de_creation',
            field=models.DateField(auto_now=True, null=True),
        ),
    ]