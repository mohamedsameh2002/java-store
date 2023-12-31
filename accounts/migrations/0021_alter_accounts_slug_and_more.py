# Generated by Django 4.2.4 on 2023-11-28 01:47

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0020_alter_accounts_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounts',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_pictuer',
            field=models.ImageField(blank=True, default='userprofile/av12154.png', null=True, upload_to=accounts.models.image_upload),
        ),
    ]
