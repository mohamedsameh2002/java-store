# Generated by Django 4.2.4 on 2023-09-21 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0017_category_category_name_ar_color_color_name_ar_and_more'),
        ('blog', '0009_blog_content_ar_blog_topic_ar_category_category_ar_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='p_products',
            field=models.ManyToManyField(blank=True, null=True, to='store.product'),
        ),
    ]
