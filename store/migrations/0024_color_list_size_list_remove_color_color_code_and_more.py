# Generated by Django 4.2.4 on 2023-10-22 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0023_color_size_size_color'),
    ]

    operations = [
        migrations.CreateModel(
            name='Color_List',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color_name', models.CharField(max_length=50)),
                ('color_name_ar', models.CharField(max_length=50)),
                ('color_code', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Size_List',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size_name', models.CharField(max_length=50)),
                ('size_name_ar', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='color',
            name='color_code',
        ),
        migrations.RemoveField(
            model_name='color',
            name='color_name',
        ),
        migrations.RemoveField(
            model_name='color',
            name='color_name_ar',
        ),
        migrations.RemoveField(
            model_name='size',
            name='size_name',
        ),
        migrations.RemoveField(
            model_name='size',
            name='size_name_ar',
        ),
        migrations.AddField(
            model_name='color',
            name='colors',
            field=models.ManyToManyField(to='store.color_list'),
        ),
        migrations.AddField(
            model_name='size',
            name='sizes',
            field=models.ManyToManyField(to='store.size_list'),
        ),
    ]
