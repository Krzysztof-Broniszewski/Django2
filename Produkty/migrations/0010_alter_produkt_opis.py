# Generated by Django 4.1 on 2022-08-31 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Produkty', '0009_alter_produkt_opis'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produkt',
            name='opis',
            field=models.TextField(),
        ),
    ]
