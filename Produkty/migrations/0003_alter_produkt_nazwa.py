# Generated by Django 4.1 on 2022-08-27 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Produkty', '0002_produkt_drzwi_produkt_kolor_produkt_silnik_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produkt',
            name='nazwa',
            field=models.CharField(max_length=120),
        ),
    ]
