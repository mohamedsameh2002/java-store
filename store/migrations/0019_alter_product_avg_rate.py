# Generated by Django 4.2.4 on 2023-10-18 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0018_product_avg_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='avg_rate',
            field=models.DecimalField(decimal_places=1, default=0.0, max_digits=2),
        ),
    ]
