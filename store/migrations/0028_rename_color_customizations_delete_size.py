# Generated by Django 4.2.4 on 2023-10-22 10:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0027_color_status_color_list_status_size_status_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Color',
            new_name='Customizations',
        ),
        migrations.DeleteModel(
            name='Size',
        ),
    ]
