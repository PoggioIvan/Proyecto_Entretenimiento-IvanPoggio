# Generated by Django 4.1.3 on 2023-01-11 15:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appa', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='avatar',
            old_name='User',
            new_name='user',
        ),
    ]
