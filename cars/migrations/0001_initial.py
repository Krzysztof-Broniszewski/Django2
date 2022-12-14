# Generated by Django 4.1.1 on 2022-10-15 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car', models.CharField(max_length=20)),
                ('model', models.CharField(max_length=20)),
                ('description', models.TextField(blank=True, null=True)),
                ('engine', models.CharField(choices=[('diesel', 'Diesel'), ('benzin', 'Benzin'), ('electric', 'Electric'), ('hybrid', 'Hybrid')], default='diesel', max_length=30)),
                ('gear_box', models.CharField(choices=[('manual', 'manual'), ('automatic', 'automatic'), ('dsg', 'dsg')], default='manual', max_length=30)),
                ('doors', models.DecimalField(decimal_places=0, default=5, max_digits=1)),
                ('price', models.DecimalField(decimal_places=2, default=1000, max_digits=10)),
            ],
        ),
    ]
