# Generated by Django 4.2.4 on 2023-10-11 22:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0017_remove_accounts_session_code_accounts_is_popup'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accounts',
            old_name='is_popup',
            new_name='is_manual',
        ),
    ]