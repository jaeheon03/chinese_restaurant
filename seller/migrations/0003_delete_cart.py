# Generated by Django 5.0.4 on 2024-04-18 01:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0002_cart'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cart',
        ),
    ]
