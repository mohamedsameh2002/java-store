# Generated by Django 4.2.4 on 2023-09-17 14:54

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_alter_userprofile_profile_pictuer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_pictuer',
            field=models.ImageField(blank=True, default='userprofile/blog-05_2SI8kgU.jpg', null=True, upload_to=accounts.models.image_upload),
        ),
    ]