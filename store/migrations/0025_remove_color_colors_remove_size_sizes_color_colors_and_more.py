# Generated by Django 4.2.4 on 2023-10-22 07:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0024_color_list_size_list_remove_color_color_code_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='color',
            name='colors',
        ),
        migrations.RemoveField(
            model_name='size',
            name='sizes',
        ),
        migrations.AddField(
            model_name='color',
            name='colors',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='store.color_list'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='size',
            name='sizes',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='store.size_list'),
            preserve_default=False,
        ),
    ]
