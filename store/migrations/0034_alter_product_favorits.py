# Generated by Django 4.2.4 on 2023-11-29 02:43

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0033_product_favorits_delete_favorite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='favorits',
            field=models.ManyToManyField(blank=True, null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]