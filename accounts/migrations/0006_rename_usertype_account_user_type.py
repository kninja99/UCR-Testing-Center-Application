# Generated by Django 3.2.16 on 2023-02-02 05:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_rename_accounts_account'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='userType',
            new_name='user_type',
        ),
    ]
