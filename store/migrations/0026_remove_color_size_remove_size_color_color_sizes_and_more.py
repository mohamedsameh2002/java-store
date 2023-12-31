# Generated by Django 4.2.4 on 2023-10-22 09:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0025_remove_color_colors_remove_size_sizes_color_colors_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='color',
            name='size',
        ),
        migrations.RemoveField(
            model_name='size',
            name='color',
        ),
        migrations.AddField(
            model_name='color',
            name='sizes',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='store.size_list'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='size',
            name='colors',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='store.color_list'),
            preserve_default=False,
        ),
    ]
