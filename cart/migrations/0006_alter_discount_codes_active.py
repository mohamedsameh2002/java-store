# Generated by Django 4.2.4 on 2023-09-19 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0005_discount_codes_cartitem_discount_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discount_codes',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
