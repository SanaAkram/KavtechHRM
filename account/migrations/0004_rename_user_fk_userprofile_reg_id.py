# Generated by Django 4.0.3 on 2022-08-17 08:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_rename_user_userprofile_user_fk'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='user_fk',
            new_name='reg_id',
        ),
    ]
