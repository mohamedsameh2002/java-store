# Generated by Django 4.2.4 on 2023-10-26 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0029_alter_customizations_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviewrating',
            name='rtl',
            field=models.BooleanField(default=True),
        ),
    ]
