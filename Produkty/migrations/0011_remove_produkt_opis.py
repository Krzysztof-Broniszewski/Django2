# Generated by Django 4.1 on 2022-08-31 18:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Produkty', '0010_alter_produkt_opis'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produkt',
            name='opis',
        ),
    ]
