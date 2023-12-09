# Generated by Django 4.2.4 on 2023-11-19 08:23

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0032_remove_favorite_by_session_delete_favorite_storeg_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='favorits',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Favorite',
        ),
    ]